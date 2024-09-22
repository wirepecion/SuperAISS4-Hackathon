# %%
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, pipeline
from datasets import load_dataset, Dataset
from trl import SFTTrainer, DataCollatorForCompletionOnlyLM
from peft import LoraConfig, prepare_model_for_kbit_training, get_peft_model
import torch
import pandas as pd
import os
import torch

dataset = pd.read_csv("your_train_dataset.csv")
dataset = Dataset.from_pandas(dataset)
pandas_eval = pd.read_csv("your_eval_dataset.csv")
dataset_eval = Dataset.from_pandas(pandas_eval)

# %%
tokenizer = AutoTokenizer.from_pretrained(
    "SeaLLMs/SeaLLM-7B-v2.5",
    trust_remote_code=True,
)
model = AutoModelForCausalLM.from_pretrained(
    "SeaLLMs/SeaLLM-7B-v2.5",
    device_map="auto",
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
)

# %%
lora_config = LoraConfig(
    r=32,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
    target_modules="all-linear",
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()

# %%
if hasattr(model.base_model, "enable_input_require_grads"):
    model.base_model.enable_input_require_grads()
elif hasattr(model.base_model, "get_input_embeddings"):

    def make_inputs_require_grad(_module, _input, _output):
        _output.requires_grad_(True)

    model.base_model.get_input_embeddings().register_forward_hook(
        make_inputs_require_grad
    )

    
def formatting_prompts_func(example):
    output_texts = []
    for i in range(len(example["context"])):
        try:
            total = len(eval(example["question"][i]))
        except:
            total = "don't know"
        messages = [
    {
        "role": "system",
        "content": "You are a Thai linguist who knows about the Thai language. Your job is to verify the authority of the Fraud Detection Committee based on the signatures provided in context. The committee whose signature is in the committee list.\nFormat task that provides:\n1. Context\nDescription of context: This includes the name of the committee and conditions.\nCommittee is a group of members with the authority, granted fairly, to sign documents.\nThe condition often takes the form of specifying the required number of committee members to sign, determining which committee group to draw from, and requiring someone to sign if the amount exceeds X baht \n2. Signs_committee\nDescription of signs_committee: The group of people who sign this document.\n3. number_of_committee \nDescription of number_of_committee: The number of signs_committee \nInstruction: Helps check whether the committee's signatures match the conditions stated earlier in the context. You should respond with 0 if they don't match, and 1 if they do. don't respond in string"
    },
    {
        "role": "user",
        "content": f"context : {example['context'][i]}.\nSigns_committee : {example['question'][i]}\n number_of_committee:{total}"
    },
    {"role": "assistant", "content": str(example["answer"][i])},
]


        text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            return_tensors="pt"
        )
        output_texts.append(text)
        

    return output_texts

response_template = "<|im_start|>assistant\n"

collator = DataCollatorForCompletionOnlyLM(response_template, tokenizer=tokenizer)


def compute_metrics(eval_pred):
    load_accuracy = load_metric("accuracy")
    load_f1 = load_metric("f1")

    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    accuracy = load_accuracy.compute(predictions=predictions, references=labels)["accuracy"]
    f1 = load_f1.compute(predictions=predictions, references=labels)["f1"]
    return {"accuracy": accuracy, "f1": f1}


# %%
trainer = SFTTrainer(
    model,
    args=TrainingArguments(
        per_device_train_batch_size=3,
        gradient_accumulation_steps=16,
        bf16=True,
        num_train_epochs=3,
        learning_rate=1e-4,
        optim="adamw_8bit",
        gradient_checkpointing=True,
        logging_strategy="steps",
        logging_steps=10,
        save_strategy="steps",
        save_steps=0.1,
        output_dir="output_seallm/",
        save_total_limit=1,
        gradient_checkpointing_kwargs={"use_reentrant":False},
        report_to="none"
    ),
    train_dataset=dataset,
    formatting_func=formatting_prompts_func,
    data_collator=collator,
    max_seq_length=4096,
    compute_metrics=compute_metrics,
    eval_dataset=dataset_eval
    # neftune_noise_alpha=5,
)

model.config.use_cache = False

trainer.train(resume_from_checkpoint=False)

# %%
model.config.use_cache = True
trainer.model.save_pretrained("your_model_name")
tokenizer.save_pretrained("your_model_name")


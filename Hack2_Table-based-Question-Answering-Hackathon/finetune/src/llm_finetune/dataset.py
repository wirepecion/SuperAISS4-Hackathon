import transformers
from datasets import load_dataset

from typing import Dict
import copy
import os

from .data_collator import DataCollatorForSupervisedDataset
from .constant import PROMPT_DICT, IGNORE_INDEX
from .tokenize import _tokenize_fn


def preprocess(tokenizer):
    def _preprocess(sample):

        if sample.get("table","") == "feedback":
            text = PROMPT_DICT["feedback"]
            source = text.format_map(sample)
            target = f"{{\"answer\": \"{sample['pandas']}\"}}{tokenizer.eos_token}"
        else:
            text = PROMPT_DICT["new"]
            source = text.format_map(sample)
            target = f"{{\"pandas\": \"{sample['pandas']}\"}}{tokenizer.eos_token}"
  
        example = source + target
        
        example_tokenized = _tokenize_fn(example, tokenizer)
        source_tokenized = _tokenize_fn(source, tokenizer)
        #print("_________________________________________________________________________________________")
        input_ids = example_tokenized["input_ids"]
        label = copy.deepcopy(input_ids)
        label[: source_tokenized["input_ids_lens"]] = IGNORE_INDEX
        return dict(
            input_ids=input_ids,
            labels=label,
        )

    return _preprocess


def load_data(path, tokenizer):
    dataset = load_dataset("json", data_files=path)["train"]
    dataset = dataset.map(preprocess(tokenizer), num_proc=os.cpu_count())

    return dataset


def make_supervised_data_module(
    tokenizer: transformers.PreTrainedTokenizer, data_args
) -> Dict:
    """Make dataset and collator for supervised fine-tuning."""
    train_dataset = load_data(data_args.train_data_path, tokenizer=tokenizer)
    eval_dataset = None
    if data_args.eval_data_path:
        eval_dataset = load_data(data_args.eval_data_path, tokenizer=tokenizer)
    data_collator = DataCollatorForSupervisedDataset(tokenizer=tokenizer)
    return dict(
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        data_collator=data_collator,
    )

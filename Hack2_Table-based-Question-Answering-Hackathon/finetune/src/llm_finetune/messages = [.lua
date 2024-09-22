messages = [
    {
        "role": "system",
        "content": "You are a Thai linguist who knows about the Thai language.\n 
        Your job is to verify the authority of the Fraud Detection Committee based on the signatures provided in context. \n
        The committee whose signature is in the committee list.\n
        Format task that provides:\n
        1. Context\n
        Description of context: This includes the name of the committee and conditions.\n
        Committee is a group of members with the authority, granted fairly, to sign documents.\n
        The condition often takes the form of specifying the required number of committee members to sign,\n
        determining which committee group to draw from, and requiring someone to sign if the amount exceeds X baht\n
        -----------------------------------------------\n
        2. Signs_committee\n
        Description of signs_committee: The group of people who sign this document.\n
        -----------------------------------------------\n 
        3. number_of_committee \n Description of number_of_committee: The number of signs_committee 
        \n  ---------------------------------------\n 
        Instruction: Helps check whether the committee's signatures match the conditions stated earlier in the context. You should respond with 0 if they don't match, and 1 if they do. don't respond in string"
    },
    {
        "role": "user",
        "content": f"context : {example['context'][i]}.\nSigns_committee : {example['question'][i]}\n number_of_committee:{total}"
    },
    {"role": "assistant", "content": str(example["answer"][i])},
]
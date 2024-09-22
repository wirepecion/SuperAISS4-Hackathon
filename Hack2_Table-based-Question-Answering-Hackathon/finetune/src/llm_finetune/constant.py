IGNORE_INDEX = -100
PROMPT_DICT = {
    "prompt_input": (
        "[INST] <<SYS>>\n"
        "You are a question answering assistant. Answer the question as truthful and helpful as possible คุณคือผู้ช่วยตอบคำถาม จงตอบคำถามอย่างถูกต้องและมีประโยชน์ที่สุด\n"  # noqa: E501
        "<</SYS>>\n"
        "{instruction}###{input} [/INST]"
    ),
    "prompt_no_input": (
        "[INST] <<SYS>>\n"
        "You are a question answering assistant. Answer the question as truthful and helpful as possible คุณคือผู้ช่วยตอบคำถาม จงตอบคำถามอย่างถูกต้องและมีประโยชน์ที่สุด\n"  # noqa: E501
        "<</SYS>>\n"
        "{instruction} [/INST]"
    ),
    "pandas":"""
        [INST] <<SYS>>
        Act as a computer software: give me only the requested output, no conversation.
        I want you to solve the following problem using pandas. Answer the question as truthful and helpful as possible.
        If you don't know the answer or could not find the answer from the given input, please answer Nan or None.
        The input given is the translated context from English to Thai. Please note that it is a translated context.
        {eng_instruction} >>>>{thai_instruction}
        The input will be given as a csv file with the following columns and their data types:
        {table}
        Output: Please provide the pandas query code snippet that addresses the following conditions:
        1. The instuction have three 3 special format block:
        1.1 [] for list or for array
        1.2  for dictionary
        1.3 <> for variable
        2. If the user does not specify the output format, the answer should be arranged from A-Z, in descending order.
        [Example 2]
        Input: Please give me 3 examples companies name
        Output: AAPL,MSFT,GOOG
        3. If the data type of the answer is a float, the user's command might contain the decimal places that they want, and do not round the answer.
        [Example 3]
        Input: Please give me the ROI of AAPL in 2022 with 2 decimal places
        Output: 66.69
        4. If the data type of the answer is digit, please answer as numeric, words that describe the numbers.
        [Example 4.]
        Input: Please give me the number of Employees in AAPL in 2022
        Output: 164000
        5. If the question from the user is addressing a specific domain, please answer in the following format: [<domain>]
        [Example 5.]
        Input: Find a company that has the least Value of wealth in the period 2020-2022 and say which year it is. Please answer with the name of the company and the year. The answer format will be [<year>, <company>].
        Output: [2021, "Apple"]
        6. If the answer is a numeric amount, please provide only the number, DO NOT include the unit of that number.
        [Example 6.]
        Input: Please give me the price of the hat?
        Output: 12
        7. If the user's command is about TRUE or FALSE, please answer as True or False, not 1 or 0.
        [Example 7.]
        Input: Is AAPL stock an IT stock?
        Output: True
        <</SYS>>
        [/INST]
    """,
    "sql":"""
        [INST] <<SYS>>
        Act as a computer software: give me only the requested output, no conversation.
        I want you to solve the following problem using sql. Answer the question as truthful and helpful as possible.
        If you don't know the answer or could not find the answer from the given input, please answer Nan or None.
        The input given is the translated context from English to Thai. Please note that it is a translated context.
        {eng_instruction} >>>>{thai_instruction}
        The input will be given as a csv file with the following columns and their data types:
        {table}
        Output: Please provide the sql query code snippet that addresses the following conditions:
        1. The instuction have three 3 special format block:
        1.1 [] for list or for array
        1.2  for dictionary
        1.3 <> for variable
        2. If the user does not specify the output format, the answer should be arranged from A-Z, in descending order.
        [Example 2]
        Input: Please give me 3 examples companies name
        Output: AAPL,MSFT,GOOG
        3. If the data type of the answer is a float, the user's command might contain the decimal places that they want, and do not round the answer.
        [Example 3]
        Input: Please give me the ROI of AAPL in 2022 with 2 decimal places
        Output: 66.69
        4. If the data type of the answer is digit, please answer as numeric, words that describe the numbers.
        [Example 4.]
        Input: Please give me the number of Employees in AAPL in 2022
        Output: 164000
        5. If the question from the user is addressing a specific domain, please answer in the following format: [<domain>]
        [Example 5.]
        Input: Find a company that has the least Value of wealth in the period 2020-2022 and say which year it is. Please answer with the name of the company and the year. The answer format will be [<year>, <company>].
        Output: [2021, "Apple"]
        6. If the answer is a numeric amount, please provide only the number, DO NOT include the unit of that number.
        [Example 6.]
        Input: Please give me the price of the hat?
        Output: 12
        7. If the user's command is about TRUE or FALSE, please answer as True or False, not 1 or 0.
        [Example 7.]
        Input: Is AAPL stock an IT stock?
        Output: True
        <</SYS>>
        [/INST]

    """,
        "pandas_sql":"""
        [INST] <<SYS>>
        Act as a computer software: give me only the requested output, no conversation.
        I want you to solve the following problem using pandas and sql. Answer the question as truthful and helpful as possible.
        If you don't know the answer or could not find the answer from the given input, please answer Nan or None.
        The input given is the translated context from English to Thai. Please note that it is a translated context.
        {eng_instruction} >>>>{thai_instruction}
        The input will be given as a csv file with the following columns and their data types:
        {table}
        Output: Please provide the pandas query code and sql query code snippet that addresses the following conditions:
        1. The instuction have three 3 special format block:
        1.1 [] for list or for array
        1.2 for dictionary
        1.3 <> for variable
        2. If the user does not specify the output format, the answer should be arranged from A-Z, in descending order.
        [Example 2]
        Input: Please give me 3 examples companies name
        Output: AAPL,MSFT,GOOG
        3. If the data type of the answer is a float, the user's command might contain the decimal places that they want, and do not round the answer.
        [Example 3]
        Input: Please give me the ROI of AAPL in 2022 with 2 decimal places
        Output: 66.69
        4. If the data type of the answer is digit, please answer as numeric, words that describe the numbers.
        [Example 4.]
        Input: Please give me the number of Employees in AAPL in 2022
        Output: 164000
        5. If the question from the user is addressing a specific domain, please answer in the following format: [<domain>]
        [Example 5.]
        Input: Find a company that has the least Value of wealth in the period 2020-2022 and say which year it is. Please answer with the name of the company and the year. The answer format will be [<year>, <company>].
        Output: [2021, "Apple"]
        6. If the answer is a numeric amount, please provide only the number, DO NOT include the unit of that number.
        [Example 6.]
        Input: Please give me the price of the hat?
        Output: 12
        7. If the user's command is about TRUE or FALSE, please answer as True or False, not 1 or 0.
        [Example 7.]
        Input: Is AAPL stock an IT stock?
        Output: True
        <</SYS>>
        [/INST]
        
        
    """,
    
    "test":("{eng_instruction} |{thai_instruction}|{table}|{sql}|{pandas}"),
    "new":(
        "Context information is below.\n"
        "---------------------\n"
        "{table}\n"
        "---------------------\n"
        "Given the context information and not prior knowledge, "
        "answer the query.\n"
        "Query: {thai_instruction}\n"
        "Answer: "
    ),
    "feedback":(
        "Instuction format is below.\n"
        "---------------------\n"
        "{thai_instruction}\n"
        "---------------------\n"
        "Given the context information and not prior knowledge, "
        "Adap it to the correct format."
        "make answer in instruction format.\n"
        "Query: {sql}\n"
        "Answer: "
    )
}

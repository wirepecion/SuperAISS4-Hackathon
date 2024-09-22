from llama_index.experimental.query_engine import PandasQueryEngine
from table_query_engine.models import QueryResponse
from llama_index.llms.vllm import Vllm
from llama_index.core import PromptTemplate


class QueryEngine:
    def __init__(self, llm, df, md):
        self.query_engine = PandasQueryEngine(df=df, llm=llm, verbose=True)
        self.md = md

    def __call__(self, query_str) -> QueryResponse:

        print("query_str----------------")
        print(query_str)

        prompt =  PromptTemplate(f"""
            Context information is below.
            ---------------------
            {self.md}
            ---------------------
            Given the context information and not prior knowledge, then answer the query.
            Query: {{query_str}}
            Answer:
        """)

        print("prompt----------------")
        print(prompt)

        self.query_engine.update_prompts({"pandas_prompt": prompt})

        try:
            response = self.query_engine.query(query_str)
            if response.response.lower in str("Pandas Output: There was an error running the output as Python code. Error message: invalid syntax").lower():
                response.response = "A prediction! wow!"
            print("response----------------")
            print(response.response)
        except Exception as e:
            print("error----------------")
            print(e)
            response.response = "ah OU! I am sorry, I could not find the answer to your query. Please try again later"

        return QueryResponse(response=response.response)


def initialize_query_engine(df, md):
# '/project/lt900053-ai2415/jack-finetune/SuperAI_LLM_FineTune/llama-small'
    llm = Vllm(model='/project/lt900053-ai2415/jack-finetune/SuperAI_LLM_FineTune/llama-small', #! from model
        tensor_parallel_size=4,
    )

    return QueryEngine(llm, df, md)
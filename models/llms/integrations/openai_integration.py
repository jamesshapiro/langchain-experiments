# os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
# Note: the above is implicitly set as an env variable by me

from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = OpenAI()

llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)

question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

result = llm_chain.run(question)
print(f'{result=}')
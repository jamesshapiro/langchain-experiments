from langchain.llms import OpenAI
from langchain.llms.loading import load_llm

llm = load_llm("llm.json")

llm.save("llm_saved.json")

llm = load_llm("llm.yaml")

llm.save("llm_saved.yaml")

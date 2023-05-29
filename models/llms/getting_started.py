from langchain.llms import OpenAI

llm = OpenAI(model_name="text-ada-001", n=2, best_of=2)
result = llm("Tell me a joke")

llm_result = llm.generate(["Tell me a joke", "Tell me a poem"]*4)

len(llm_result.generations)

result = llm_result.generations[0]
print(f"{result=}")
result = llm_result.generations[-1]
print()
print(f"{result=}")
print()
print (llm_result.llm_output)
print()
print(llm.get_num_tokens("what a joke"))
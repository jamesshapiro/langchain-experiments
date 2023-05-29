from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

llm = OpenAI(model_name="text-davinci-002", n=2, best_of=2)

with get_openai_callback() as cb:
    result = llm("Tell me a joke")
    print(f'{cb=}')

with get_openai_callback() as cb:
    result = llm("Tell me a joke")
    result2 = llm("Tell me a joke")
    print(f'{cb.total_tokens=}')

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

llm = OpenAI(temperature=0)
tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

with get_openai_callback() as cb:
    response = agent.run("Who won the Super Bowl the year that COVID became a pandemic?")
    print(f"Total Tokens: {cb.total_tokens}")
    print(f"Prompt Tokens: {cb.prompt_tokens}")
    print(f"Completion Tokens: {cb.completion_tokens}")
    print(f"Total Cost (USD): ${cb.total_cost}")
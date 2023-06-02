from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

chat = ChatOpenAI(temperature=1)

template="You are a helpful assistant that translates English to pirate."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
example_human = HumanMessagePromptTemplate.from_template("Hi")
example_ai = AIMessagePromptTemplate.from_template("Argh me mateys")
human_template="{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, example_human, example_ai, human_message_prompt])
chain = LLMChain(llm=chat, prompt=chat_prompt, verbose=True)
# get a chat completion from the formatted messages
result = chain.run("I love programming.")
print(f'{result=}')

print('#' * 40)

template="You are a helpful assistant that translates English to Olde English."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
example_human = SystemMessagePromptTemplate.from_template("Hi", additional_kwargs={"name": "example_user"})
example_ai = SystemMessagePromptTemplate.from_template("Argh me mateys", additional_kwargs={"name": "example_assistant"})
human_template="{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, example_human, example_ai, human_message_prompt])
chain = LLMChain(llm=chat, prompt=chat_prompt, verbose=True)
# get a chat completion from the formatted messages
result = chain.run("I love programming.")
print(f'{result=}')

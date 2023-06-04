from langchain.chat_models import ChatOpenAI
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

from langchain.llms import OpenAI

llm = OpenAI(model_name="text-ada-001", n=2, best_of=2)

messages = [
    SystemMessage(content="You are a helpful assistant that translates English to Pig Latin."),
    HumanMessage(content="Translate this sentence from English. I enjoy programming.")
]
result = chat(messages)
print(f'{result=}')

print('#' * 40)
template="You are a helpful assistant that translates {input_language} to {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template="{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
# get a chat completion from the formatted messages
result = chat(chat_prompt.format_prompt(input_language="English", output_language="Pig Latin", text="I like programming a lot. Hello world.").to_messages())
print(f'{result=}')

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

chat = ChatOpenAI(temperature=0.5)

result = chat([HumanMessage(content="You are a masterful English-to-French translator. Translate the following text to French: I am a programmer.")])
# -> AIMessage(content="J'aime programmer.", additional_kwargs={})

print(f'{result=}')

messages = [
    SystemMessage(content="You are a masterful English-to-French translator."),
    HumanMessage(content="I love programming.")
]
result = chat(messages)
print(f'{result=}')


batch_messages = [
    [
        SystemMessage(content="You are a helpful assistant that translates English to French."),
        HumanMessage(content="I love programming.")
    ],
    [
        SystemMessage(content="You are a helpful assistant that translates English to French."),
        HumanMessage(content="I love artificial intelligence.")
    ],
]
result = chat.generate(batch_messages)
print(f'{result=}')
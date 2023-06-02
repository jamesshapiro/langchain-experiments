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

chat = ChatOpenAI(temperature=0)

result = chat([HumanMessage(content="Translate this sentence from English to French. I love programming.")])
print(f'{result=}')

messages = [
    SystemMessage(content="You are a helpful assistant that translates English to French."),
    HumanMessage(content="Hello world!")
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

print(f'{result.llm_output=}')

print('#' * 40)

template="You are a helpful assistant that translates {input_language} to {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template="{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

# get a chat completion from the formatted messages
result = chat(chat_prompt.format_prompt(input_language="English", output_language="French", text="I love programming.").to_messages())
print(f'{result=}')

# Alternatively:
# prompt=PromptTemplate(
#     template="You are a helpful assistant that translates {input_language} to {output_language}.",
#     input_variables=["input_language", "output_language"],
# )
# system_message_prompt = SystemMessagePromptTemplate(prompt=prompt)

chain = LLMChain(llm=chat, prompt=chat_prompt)
result = chain.run(input_language="English", output_language="Russian", text="I love programming.")
print(f'{result=}')

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
chat = ChatOpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=0)
print('#' * 40)
resp = chat([HumanMessage(content="Write me a song about sparkling water from Russia.")])
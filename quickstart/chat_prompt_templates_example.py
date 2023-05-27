from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

chat = ChatOpenAI(temperature=0.5)

template = "You are a masterful translator that translates {input_language} to {output_language}."

system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{text}"

human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

# get a chat completion from the formatted messages
result = chat(chat_prompt.format_prompt(input_language="English", output_language="Russian", text="I love programming.").to_messages())
print(f'{result=}')
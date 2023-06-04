from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

template="You are a helpful assistant that translates {input_language} to {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template="{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

# Alternatively:
prompt=PromptTemplate(
    template="You are a helpful assistant that translates {input_language} to {output_language}.",
    input_variables=["input_language", "output_language"],
)
system_message_prompt_2 = SystemMessagePromptTemplate(prompt=prompt)
assert system_message_prompt == system_message_prompt_2
# END

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
# get a chat completion from the formatted messages
print(chat_prompt.format_prompt(input_language="English", output_language="French", text="I enjoy programming.").to_messages())


print('#'*80)
output = chat_prompt.format(input_language="English", output_language="French", text="I enjoy programming.")
print(output)

# Alternatively:
output_2 = chat_prompt.format_prompt(input_language="English", output_language="French", text="I enjoy programming.").to_string()
assert output == output_2

print('#'*80)
print(chat_prompt.format_prompt(input_language="English", output_language="Russian", text="I enjoy programming."))

print('#'*80)
print(chat_prompt.format_prompt(input_language="English", output_language="French", text="I enjoy programming.").to_messages())


print('#'*80)
from langchain.prompts import ChatMessagePromptTemplate
prompt = "Here is a prompt from a custom role about {subject}"
chat_message_prompt = ChatMessagePromptTemplate.from_template(role="Clown", template=prompt)
print(chat_message_prompt.format(subject="cars"))

print('#'*80)
from langchain.prompts import MessagesPlaceholder
human_prompt = "Summarize our conversation so far in {word_count} words."
human_message_template = HumanMessagePromptTemplate.from_template(human_prompt)
chat_prompt = ChatPromptTemplate.from_messages([MessagesPlaceholder(variable_name="conversation"), human_message_template])

human_message = HumanMessage(content="What is the best way to learn programming?")
ai_message = AIMessage(content="""\
1. Choose a programming language: Decide on a programming language that you want to learn. 

2. Start with the basics: Familiarize yourself with the basic programming concepts such as variables, data types and control structures.

3. Practice, practice, practice: The best way to learn programming is through hands-on experience\
""")
print(chat_prompt.format_prompt(conversation=[human_message, ai_message], word_count="10").to_messages())
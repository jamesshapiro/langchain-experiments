from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

llm = OpenAI()

from langchain.schema import HumanMessage, AIMessage
result = llm.predict_messages([HumanMessage(content="say hi!"), AIMessage(content="Hi there!")])
#result = llm.predict_messages([HumanMessage(content="say hi!"), AIMessage(content="Hi there!"), HumanMessage(content="Shalom Haverim!")])

# Note: blank response if the last message is an AIMessage
print(f'{result=}')

#chat_model.predict_messages([HumanMessage(content="say hi!")])
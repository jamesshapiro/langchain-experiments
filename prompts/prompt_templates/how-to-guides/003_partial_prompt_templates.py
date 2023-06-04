from langchain.prompts import PromptTemplate

# Partial With Strings

prompt = PromptTemplate(template="{foo}{bar}", input_variables=["foo", "bar"])
partial_prompt = prompt.partial(foo="foo");
print(partial_prompt.format(bar="baz"))

print('#'*80)
prompt = PromptTemplate(template="{foo}{bar}", input_variables=["bar"], partial_variables={"foo": "froo"})
print(prompt.format(bar="brar"))

print('#'*80)

# Partial With Functions

from datetime import datetime

def _get_datetime():
    now = datetime.now()
    return now.strftime("%m-%d-%Y")

prompt = PromptTemplate(
    template="Tell me the weather in {location} on {date}", 
    input_variables=["location", "date"]
)
partial_prompt = prompt.partial(date=_get_datetime)
print(partial_prompt.format(location="Miami"))

print('#'*80)

prompt = PromptTemplate(
    template="Tell me the weather in {location} on {date}", 
    input_variables=["location"],
    partial_variables={"date": _get_datetime}
)
print(prompt.format(location="Zug"))
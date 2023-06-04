# All prompts are loaded through the `load_prompt` function.
from langchain.prompts import load_prompt

prompt = load_prompt("simple_prompt.yaml")
print(prompt.format(adjective="funny", content="chickens"))

print('#'*80)
prompt = load_prompt("simple_prompt.json")
print(prompt.format(adjective="funny", content="chickens"))

print('#'*80)
prompt = load_prompt("few_shot_prompt.yaml")
print(prompt.format(adjective="funny"))

print('#'*80)
prompt = load_prompt("few_shot_prompt_yaml_examples.yaml")
print(prompt.format(adjective="funny"))

print('#'*80)
prompt = load_prompt("few_shot_prompt.json")
print(prompt.format(adjective="funny"))

print('#'*80)
prompt = load_prompt("few_shot_prompt_json_examples.json")
print(prompt.format(adjective="funny"))

print('#'*80)
prompt = load_prompt("few_shot_prompt_example_prompt.json")
print(prompt.format(adjective="funny"))

print('#'*80)
prompt = load_prompt("prompt_with_output_parser.json")
print(prompt.output_parser.parse("George Washington was born in 1732 and died in 1799.\nScore: 1/2"))

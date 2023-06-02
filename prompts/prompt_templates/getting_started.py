from langchain import PromptTemplate


template = """
I want you to act as a naming consultant for new companies.
What is a good name for a company that makes {product}?
"""

prompt = PromptTemplate(
    input_variables=["product"],
    template=template,
)
prompt.format(product="cool cats")

# An example prompt with no input variables
no_input_prompt = PromptTemplate(input_variables=[], template="Tell me a joke.")
no_input_prompt.format()
# -> "Tell me a joke."

# An example prompt with one input variable
one_input_prompt = PromptTemplate(input_variables=["adjective"], template="Tell me a {adjective} joke.")
one_input_prompt.format(adjective="funny")
# -> "Tell me a funny joke."

# Note: variables can be inferred from the template using the .from_template() method
template = "Tell me a {adjective} joke about {content}."
prompt_template = PromptTemplate.from_template(template)
prompt_template.input_variables
# -> ['adjective', 'content']
prompt_template.format(adjective="funny", content="chickens")
# -> Tell me a funny joke about chickens.


# Using other templates. E.g. jinja2
jinja2_template = "Tell me a {{ adjective }} joke about {{ content }}"
prompt_template = PromptTemplate.from_template(template=jinja2_template, template_format="jinja2")
prompt_template.format(adjective="funny", content="chickens")
# -> Tell me a funny joke about chickens.



template = "I am learning langchain because {reason}."
try:
    # ValueError due to extra variables
    prompt_template = PromptTemplate(template=template, 
                                     input_variables=["reason", "foo"])
except ValueError as e:
    print('As expected: Invalid prompt schema; check for mismatched or missing input parameters. {"foo"} (type=value_error)')
prompt_template = PromptTemplate(template=template, 
                                 input_variables=["reason", "foo"], 
                                 validate_template=False) # No error

prompt_template.save("awesome_prompt.json")
from langchain.prompts import load_prompt
loaded_prompt = load_prompt("awesome_prompt.json")

assert prompt_template == loaded_prompt


# Loading a prompt from LangChainHub
from langchain.prompts import load_prompt
prompt = load_prompt("lc://prompts/conversation/prompt.json")
result = prompt.format(history="", input="What is 1 + 1?")
print(prompt)



#Pass few shot examples to a prompt template
from langchain import FewShotPromptTemplate
# First, create the list of few shot examples.
examples = [
    {"word": "happy", "antonym": "sad"},
    {"word": "tall", "antonym": "short"},
]

# Next, we specify the template to format the examples we have provided.
# We use the `PromptTemplate` class for this.
example_formatter_template = """Word: {word}
Antonym: {antonym}
"""

example_prompt = PromptTemplate(
    input_variables=["word", "antonym"],
    template=example_formatter_template,
)

# Finally, we create the `FewShotPromptTemplate` object.
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="Give the antonym of every input\n",
    # The suffix is some text that goes after the examples in the prompt.
    # Usually, this is where the user input will go
    suffix="Word: {input}\nAntonym: ",
    # The input variables are the variables that the overall prompt expects.
    input_variables=["input"],
    # The example_separator is the string we will use to join the prefix, examples, and suffix together with.
    example_separator="\n",
)

print('\n' + '#' * 40 + '\n')
print(few_shot_prompt.format(input="big"))
print('\n' + '#' * 40 + '\n')

from langchain.prompts.example_selector import LengthBasedExampleSelector
# These are a lot of examples of a pretend task of creating antonyms.
examples = [
    {"word": "happy", "antonym": "sad"},
    {"word": "tall", "antonym": "short"},
    {"word": "energetic", "antonym": "lethargic"},
    {"word": "sunny", "antonym": "gloomy"},
    {"word": "windy", "antonym": "calm"},
]

# We'll use the `LengthBasedExampleSelector` to select the examples.
example_selector = LengthBasedExampleSelector(
    examples=examples, 
    example_prompt=example_prompt, 
    max_length=20
)

# We can now use the `example_selector` to create a `FewShotPromptTemplate`.
# Note how it seems to cut off the examples after the third one.
dynamic_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix="Give the antonym of every input",
    suffix="Word: {input}\nAntonym:",
    input_variables=["input"],
    example_separator="\n\n",
)

print(dynamic_prompt.format(input="big"))
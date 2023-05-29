import langchain
from langchain.llms import OpenAI

# To make the caching really obvious, lets use a slower model.
llm = OpenAI(model_name="text-davinci-002", n=2, best_of=2)

from langchain.cache import InMemoryCache
langchain.llm_cache = InMemoryCache()

import time

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time}")
        return result
    return wrapper

@timing_decorator
def run_llm(prompt):
    return llm(prompt)

first_prompt = "Tell me a joke"

result = run_llm(first_prompt)
print(f'{result=}')
result = run_llm(first_prompt)
print(f'{result=}')

print('#'*50)

from langchain.cache import SQLiteCache
langchain.llm_cache = SQLiteCache(database_path=".langchain.db")

second_prompt = "Tell me a yo momma joke"

# The first time, it is not yet in cache, so it should take longer
result = run_llm(second_prompt)
print(f'{result=}')
result = run_llm(second_prompt)
print(f'{result=}')
print('#'*50)

# from redis import Redis
# from langchain.cache import RedisCache

# langchain.llm_cache = RedisCache(redis_=Redis())

# third_prompt = "Tell me a knock knock joke"
# result = run_llm(third_prompt)
# print(f'{result=}')
# result = run_llm(third_prompt)
# print(f'{result=}')


from gptcache import Cache
from gptcache.manager.factory import manager_factory
from gptcache.processor.pre import get_prompt
from gptcache.adapter.api import init_similar_cache
from langchain.cache import GPTCache
import hashlib

def get_hashed_name(name):
    return hashlib.sha256(name.encode()).hexdigest()

# def init_gptcache(cache_obj: Cache, llm: str):
#     hashed_llm = get_hashed_name(llm)
#     cache_obj.init(
#         pre_embedding_func=get_prompt,
#         data_manager=manager_factory(manager="map", data_dir=f"map_cache_{hashed_llm}"),
#     )

def init_gptcache(cache_obj: Cache, llm: str):
    hashed_llm = get_hashed_name(llm)
    init_similar_cache(cache_obj=cache_obj, data_dir=f"similar_cache_{hashed_llm}")

langchain.llm_cache = GPTCache(init_gptcache)

fourth_prompt = "Tell me a joke"
fourth_alternative_prompt = "Tell me one joke"
fourth_another_prompt = "Tell me some joke"
fourth_yet_another_prompt = "Tell me any joke"

result = run_llm(fourth_prompt)
print(f'{result=}')
result = run_llm(fourth_alternative_prompt)
print(f'{result=}')
result = run_llm(fourth_another_prompt)
print(f'{result=}')
result = run_llm(fourth_yet_another_prompt)
print(f'{result=}')
result = run_llm(fourth_prompt)
print(f'{result=}')
print('#'*50)

# Example: turning off caching for a specific model
llm = OpenAI(model_name="text-davinci-002", n=2, best_of=2, cache=False)

result = run_llm(first_prompt)
print(f'{result=}')
result = run_llm(first_prompt)
print(f'{result=}')
print('#'*50)
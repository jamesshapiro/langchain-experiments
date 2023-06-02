from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
text = "This is a test document."
query_result = embeddings.embed_query(text)
doc_result = embeddings.embed_documents([text])
print(f'{query_result=}')
print(f'{doc_result=}')

print('#' * 40)

text = "This is some test document."
query_result = embeddings.embed_query(text)
doc_result = embeddings.embed_documents([text])
print(f'{query_result=}')
print(f'{doc_result=}')
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',              #folder/Directory name
    glob='*.pdf',              #which file are you wnat to load text/pdf
    loader_cls=PyPDFLoader
)
 
docs = loader.load()
#docs = loader.lazy_load()

print(docs[0].page_content)
print(docs[0].metadata)

# for document in docs:
#     print(document.metadata)

for item in docs:
    print(item.metadata)
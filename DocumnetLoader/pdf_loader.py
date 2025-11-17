from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load() #set of documents obejcts

#print(docs)
print(len(docs))

print(docs[1].page_content)
# print(docs[1].metadata)
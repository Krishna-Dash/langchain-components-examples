from langchain.document_loaders import TextLoader
from  langchain.TextSplitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate

#Load the document
Loader=TextLoader('docs.txt')
documents=Loader.load()

#spilt the text into smaller chunks
text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
docs=text_splitter.split_documents(documents)

#conerts the text into embeddings and stores them in a vector database
VectorStore=FAISS.from_documents(docs,OpenAIEmbeddings())

#create a retriever (fetches relevant documents from the vector database based on a query)
retriever=VectorStore.as_retriever()

#Mannually Retrive relevant documents
query="what are the key takeaways from the document?"
relevant_docs=retriever.get_relevant_documents(query)

#Combine Retriver Text into a single Prompt
retrieved_text="\n".join([doc.page_content for doc in relevant_docs])

#initialize the LLM
llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# mannnually pass the retiver text into llm
prompt=PromptTemplate(
    input_variables=["retrieved_text","query"],
    template="Based on the following document text, answer the question.\n\nDocument Text:\n{retrieved_text}\n\nQuestion: {query}\n\nAnswer:"
)
answer=llm.predict(prompt)

# print the answer
print(answer)
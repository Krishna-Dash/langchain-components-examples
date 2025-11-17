from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import RetrievalQAChain
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# load the document
loader = TextLoader('docs.txt')
documents = loader.load()
# split the text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(documents)

#converts the text into embeddings and stores in FAISS (Vector DB)
VectoreStores = FAISS.from_documents(docs, OpenAIEmbeddings())  

#create a retriver (this fetechs relevant documents)
retriever = VectoreStores.as_retriever()

#initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# create the RetrievalQAChain
qa_chain = RetrievalQAChain.from_chain_type(
    llm=llm, retriever=retriever)

# ask a question
query = "what are the key takeaways from the document?"
result = qa_chain.invoke({'query': query})

# print the answer
print(result['result'])
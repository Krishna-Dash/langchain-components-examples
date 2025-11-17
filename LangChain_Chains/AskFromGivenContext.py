from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Define the model (using gemini-2.0-flash for better quota)
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

context = """
When Lord Krishna was a child in Gokul, he was known for his playful and mischievous nature. 
He loved butter more than anything else and would often sneak into the houses of Gopis to steal it. 
The Gopis would hang the butter pots high from the ceiling to keep them out of his reach. 
But clever little Krishna would form a pyramid with his friends, climb on top, and reach the pot. 
Once, when his mother Yashoda caught him with butter smeared all over his face, she tried to scold him. 
Krishna ran away, but Yashoda managed to catch him and tied him to a wooden mortar as punishment. 
However, when Krishna moved, the mortar got stuck between two trees and pulled them down, 
revealing two divine beings who were freed from a curse because of Krishna’s touch. 
This incident reminded everyone that even though Krishna looked like a naughty child, 
he was truly the Supreme Lord in human form.

"""

# Template for question answering
qa_prompt = PromptTemplate(
    template="""
You are a helpful assistant. Use only the given context to answer the question.
If the answer is not in the context, say "The answer is not available in the given text."

Context:
{text}

Question: {question}
Answer:
""",
    input_variables=["text", "question"]
)

parser = StrOutputParser()

chain = qa_prompt | model | parser


print("Jai Shri Krishna! Ask any question about the story (type 'exit' to stop)")
while True:
    question = input("\nYour Question: ")
    if question.lower() == 'exit':
        print("Exiting the chat. Hare Krishna!")
        break
    if not question:
        continue

    try:
        answer = chain.invoke({"text": context, "question": question})
        print("💠 Answer:", answer, "\n")
    except Exception as e:
        print("⚠️ Something went wrong:", e, "\n")


# result = chain.invoke({'text': context, 'question': question})
# print("\n Answer:\n", result)

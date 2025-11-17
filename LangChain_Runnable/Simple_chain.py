from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

model=ChatGoogleGenerativeAI(model="gemini-2.5-pro")

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'krishna'})

print(result)

chain.get_graph().print_ascii()     #for graphical representation of chain

# chain.get_graph().print_ascii()

#previosly we invoke prompt the invoke model pass the  prompt then result.content but  with the help ofchains no need to do thoes thing only we need to pass start input to chain and it will handle every thing internally and give the final output.
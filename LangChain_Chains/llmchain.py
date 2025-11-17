from langchain.llm import google_genai
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# load the llm
llm=google_genai.ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# create the prompt
prompt = PromptTemplate(
    input_variables=["topic"],
    template="suggest a catchy blog tittle about : {topic}"
)

# create the llm chain  no need of prompt.format(topic=topic) nor llm.predict(prompt)
chain = LLMChain(llm=llm, prompt=prompt)

topic=input("Enter the blog topic: ")
output=chain.invoke({"topic":topic})    

print("Generated blog Tittle:",output)
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)
parser = StrOutputParser()

url = 'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7w4hn-a/p/itm2ea42dec44bca?pid=COMH64PYZU4ZZR79&lid=LSTCOMH64PYZU4ZZR79AHLYXY&marketplace=FLIPKART&cmpid=content_computer_22927808323_g_8965229628_gmc_pla&tgi=sem,1,G,11214002,g,search,,770553264708,,,,c,,,,,,,&entryMethod=22927808323&&cmpid=content_22927808323_gmc_pla&gad_source=1&gad_campaignid=22927808323&gbraid=0AAAAADxRY5-4EOyTbOzYRDMaRloX5n08T&gclid=Cj0KCQiAiebIBhDmARIsAE8PGNLx5A7xrA83d-XG_LtwKo5FfizF6wbowC6srqEC0Hyl_vCIO26f_usaArQUEALw_wcB'

loader = WebBaseLoader(url)
docs = loader.load()

# print(docs[0].page_content)
chain = prompt | model | parser

print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))
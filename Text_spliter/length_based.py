from langchain_text_splitters import CharacterTextSplitter


text="""In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the actual content is available. The passage is attributed to an unknown typesetter in the 15th century who is thought to have"""

splitter = CharacterTextSplitter(
    chunk_size=20,
    chunk_overlap=0,
    separator=''
)

result= splitter.split_text(text)
print(result[0])


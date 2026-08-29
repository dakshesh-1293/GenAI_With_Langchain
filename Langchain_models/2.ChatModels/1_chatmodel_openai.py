from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-5.6')

result = model.invoke("Sugest me 5 indian male names")

print(result)
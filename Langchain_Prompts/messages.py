from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro-0813",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HF_TOKEN")
)

model = ChatHuggingFace(llm=llm)
 
messages = [
     SystemMessage(content="You are a helpful assistant"),
     HumanMessage(content="Give me 5 line history on M.S. Dhoni")
 ]
 
result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)
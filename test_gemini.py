import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
# Key is now loaded from .env file automatically

# Initialize the model
llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash")

# Test it
response = llm.invoke("Say hello in exactly 3 words.")
print(response.content[0]["text"])
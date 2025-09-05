from dotenv import load_dotenv
import os
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
llm = GoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=api_key,
    temperature=0.5
)
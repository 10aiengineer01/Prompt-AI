from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

class setup_models:

    def __init__(self, model_provider, model_name=None) -> None:
        load_dotenv()
        if model_provider=="groq":
            api_key=os.getenv("GROQ_API_KEY")
            if model_name:
                self.llm = ChatGroq(api_key=api_key, model=model_name)
            else:
                self.llm = ChatGroq(api_key=api_key, model="llama3-70b-8192")
                print("Groq Model set to: llama3-70b-8192")
        elif model_provider=="openai":
            api_key=os.getenv("OPENAI_API_KEY")
            if model_name:
                self.llm = ChatOpenAI(api_key=api_key, model=model_name)
            else:
                self.llm = ChatOpenAI(api_key=api_key, model="gpt-4-turbo")
                print("Openai Model set to: gpt-4-turbo")
        else:
            print("Model provider not available.")

    def get_llm(self):
        return self.llm

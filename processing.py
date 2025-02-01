from fastapi import FastAPI
import openai
import fitz  # PyMuPDF

app = FastAPI()

# Set your OpenAI API key here
OPENAI_API_KEY = "your-openai-api-key"
openai.api_key = OPENAI_API_KEY

@app.get("/")
def home():
    return {"message": "Welcome to the AI Legal Chatbot!"}
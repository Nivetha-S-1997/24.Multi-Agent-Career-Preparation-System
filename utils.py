from dotenv import load_dotenv
import os
from PyPDF2 import PdfReader
import json
import ast

load_dotenv()
gemini_key = os.getenv('GEMINI_API_KEY')
llm_config = {'model':'gemini-2.5-flash', 'api_key':gemini_key, 'api_type':'google'}

# 1. Extract text from PDF
def pdf_reader_func(file):
    pdf_reader = PdfReader(file)
    text = ""

    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

# 2. Convert LLM string output to dictionary
def string_to_dict(reply):
    # Extract the content from the LLM reply
    if isinstance(reply, dict) and "content" in reply:
        cleaned_reply = reply["content"]
    else:
        cleaned_reply = str(reply)

    # Remove markdown formatting if present
    cleaned_reply = (
        cleaned_reply
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    # First, try parsing as JSON
    try:
        return json.loads(cleaned_reply)

    # If JSON fails, try parsing as a Python dictionary
    except json.JSONDecodeError:
        try:
            return ast.literal_eval(cleaned_reply)

        except (ValueError, SyntaxError):
            print("Failed to parse response.")
            print("Raw reply was:\n", cleaned_reply)
            return {}
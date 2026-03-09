from PyPDF2 import PdfReader
import json
import os
from dotenv import load_dotenv

load_dotenv()
gemini_key=os.getenv('GEMINI_API_KEY')
llm_config={'model':'gemini-2.5-flash',
            'api_key':gemini_key,
            'api_type':'google'}

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

    cleaned_reply = reply['content'].replace("```json", "").replace("```", "").strip()

    try:
        dict_output = json.loads(cleaned_reply)
        return dict_output

    except json.JSONDecodeError:
        print("JSON decoding failed.")
        return {}

# 3. Flatten skills dictionary into list
def flatten_skills(skill_dict):

    skills = []

    for value in skill_dict.values():
        skills.extend(value)

    return skills
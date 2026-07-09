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
        cleaned_reply.replace("```json", "").replace("```", "").strip()
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

#3. Convert a dictionary into a human-readable string for skill gap analyzer:
def format_skill_gap(data):
    """
    Converts a dictionary into a human-readable string.
    Handles nested dictionaries and lists.
    """

    output = []

    for key, value in data.items():
        output.append(f"**{key}**\n")
        output.append("") # Blank line after each section
        
        if isinstance(value, list):
            if len(value) == 0:
                output.append("None")
            else:
                for item in value:
                    output.append(f"- {item}")
            output.append("")

        elif isinstance(value, dict):
            for sub_key, sub_value in value.items():
                output.append(f"- {sub_key}: {sub_value}")
            output.append("")

        else:
            output.append(str(value))
            output.append("")

    output.append("")

    return "\n".join(output)

#3. Convert a dictionary into a human-readable string for interview question generator:
def format_interview_questions(data):
    output = []

    for category, questions in data.items():

        output.append(f"**{category}**")
        output.append("")

        for i, q in enumerate(questions, start=1):
            output.append(f"{i}. {q['question']}")
            output.append(f"   Level: {q['level']}")
            output.append("")

    return "\n".join(output)
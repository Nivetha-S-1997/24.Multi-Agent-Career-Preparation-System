# Multi-Agent Career Preparation System (AI Agents + Streamlit)
This project is a **Multi-Agent Career Preparation System** built using **Python, AutoGen, Gemini API, and Streamlit**.

It helps users evaluate and improve their resume against a Job Description (JD) by identifying skill gaps, calculating resume-job matching scores, suggesting resume improvements, and generating interview questions.

## Features
✅ Resume Parsing (PDF Upload)
✅ Structured Resume Analysis
✅ Job Description (JD) Analysis
✅ Skill Gap Detection
✅ Resume–JD Matching Score
✅ Resume Strength Identification
✅ Personalized Improvement Guidelines
✅ Resume Optimization Suggestions
✅ Interview Question Generation

## Tech Stack
- Python
- Streamlit
- AutoGen (Multi-Agent Framework)
- Gemini API
- PyPDF2
- python-dotenv

## Project Structure
Capstone Project/
│── app.py
│── career_pipeline.py
│── utils.py
│── requirements.txt
│── README.md
│── AI_agents/
│   ├── Resume_analyzer.py
│   ├── JD_extractor.py
│   ├── Skillgap_analyzer.py
│   ├── Resume_optimizer.py
│   └── Question_generator.py

## Agent Workflow
```text
Resume Upload (PDF)
        │
        ▼
Resume Analyzer Agent
        │
        ▼
JD Analyzer Agent
        │
        ▼
Skill Gap Detection Agent
        │
        ▼
Resume Optimizer Agent
        │
        ▼
Interview Question Generator Agent
        │
        ▼
Results displayed in Streamlit
```

## How to Run the Project
### Step 1: Install Dependencies
pip install -r requirements.txt

### Step 2: Run the Streamlit Application
streamlit run app.py

## Output
The Streamlit application displays:
- Resume–JD Matching Scores
- Skill Gap Analysis
- Resume Strengths
- Personalized Improvement Guidelines
- Resume Optimization Suggestions
- Interview Questions



**Author**
**Nivetha**
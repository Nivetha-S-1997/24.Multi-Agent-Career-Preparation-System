# Multi-Agent Career Preparation System (AI Agents + Streamlit)

This project is a **Multi-Agent Career Preparation System** built using **Python, AutoGen Agents, and Streamlit**.

It helps users improve their resume based on a Job Description (JD) by identifying skill gaps, suggesting resume improvements, and generating interview questions.

## Features

✅ Resume Parsing (PDF Upload)  
✅ Job Description (JD) Analysis  
✅ Skill Gap Detection  
✅ Resume Improvement Suggestions (Structured JSON Output)  
✅ Interview Question Generation based on JD  

## Project Structure
Capstone Project/
│── app.py
│── career_pipeline.py
│── utils.py
│── requirements.txt
│── README.md
│── AI_agents/
│ ├── Resume_analyzer.py
│ ├── JD_extractor.py
│ ├── Skill_gap_analyzer.py
│ ├── Resume_optimizer.py
│ ├── Interview_question_generator.py

## How to Run the Project

**Step 1: Install Dependencies**

pip install -r requirements.txt

**Step 2: Run Streamlit App**
streamlit run app.py

How It Works (Agent Workflow)

 Resume Upload
     ⬇️
 Resume Analyzer Agent
     ⬇️
 JD Analyzer Agent
     ⬇️
 Skill Gap Agent
     ⬇️
 Resume Optimizer Agent
     ⬇️
 Interview Question Generator Agent

**Output**

The Streamlit app displays:

1. Skill Gap Analysis
2. Resume Improvement Suggestions (Original vs Improved points)
3. Interview Questions based on JD



**Author**
**Nivetha**
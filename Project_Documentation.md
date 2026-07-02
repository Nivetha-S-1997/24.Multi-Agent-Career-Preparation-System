# Project Documentation - Multi-Agent Career Preparation System

## 1. Project Overview
This project is a **Multi-Agent Career Preparation System** that assists job seekers in evaluating and improving their resumes against a given Job Description (JD). It analyzes the resume, identifies skill gaps, calculates resume-job matching scores, recommends truthful resume improvements, and generates interview questions tailored to both the candidate's profile and the target role.

The system is built using a **Multi-Agent AI architecture** with a **Streamlit** interface for an interactive user experience.

## 2. Problem Statement
Many job applicants struggle to understand how well their resume aligns with a specific job description. Existing keyword-based systems often fail to consider demonstrated competencies, transferable skills, and project experience.

This project addresses that challenge by using specialized AI agents to perform structured resume analysis, compare it with job requirements, identify meaningful gaps, recommend truthful improvements, and generate personalized interview questions.

## 3. Tech Stack Used
- **Programming Language:** Python  
- **Frontend/UI:** Streamlit  
- **AI Agent Framework:** AutoGen (Multi-Agent Architecture)  
- **LLM API:** Gemini API 
- **Resume Processing:** PyPDF2  
- **Environment Variables:** python-dotenv  
- **Utilities:** JSON parsing, text processing  

## 4. High Level System Architecture
Resume (PDF)
↓
Resume Text Extraction
↓
Resume Analyzer Agent
↓
Job Description
↓
JD Analyzer Agent
↓
Skill Gap Detection Agent
↓
Resume Optimizer Agent
↓
Interview Question Generator Agent
↓
Results displayed in Streamlit UI

## 5. Multi-Agent Workflow
### Step 1 – Resume Extraction
The uploaded PDF resume is converted into plain text using PyPDF2.

### Step 2 - Resume Analyzer Agent
The Resume Analyzer extracts structured information from the resume without modifying or optimizing its content.

It extracts:
- Name
- Summary
- Work Experience
- Skills
- Tools
- Projects
- Education
- Certifications

Additionally, it identifies semantic information including:
- Demonstrated Competencies from work experience
- Technologies Used in projects
- Demonstrated Concepts from projects

### Step 3 - Job Description Extractor Agent
The JD Analyzer extracts structured hiring requirements from the Job Description.

It identifies:
- Required Skills
- Required Tools
- Preferred Skills
- Preferred Tools
- Experience Expectations
- Project Expectations
- Education Requirements

The extracted information is preserved as structured JSON for downstream comparison.

### Step 4 - Skill Gap Detection Agent
The Skill Comparator compares the structured Resume and JD outputs.

It identifies:
- Matching Required Skills
- Missing Required Skills
- Matching Required Tools
- Missing Required Tools
- Matching Preferred Skills
- Missing Preferred Skills
- Matching Preferred Tools
- Missing Preferred Tools
- Matching Experience Expectations
- Missing Experience Expectations
- Matching Project Expectations
- Missing Project Expectations

It also calculates:
- Required Score
- Preferred Score
- Experience Relevance Score
- Project Relevance Score
- Overall Resume Match Score

The Overall Score is calculated using weighted scoring, with automatic redistribution of weights when a scoring category is not applicable.

The agent additionally provides:
- Resume Strengths
- Personalized Improvement Guidelines

### Step 5 - Resume Optimizer Agent
The Resume Optimizer uses:
- Resume Analyzer output
- JD Analyzer output
- Skill Comparator output

It suggests improvements only where meaningful improvements are possible.

Each suggestion includes:
- Section
- Original Resume Content
- Improved Resume Content
- Reason for Improvement

The optimizer preserves factual information and never invents skills, experience, tools, certifications, or achievements.

### Step 6 - Interview Question Generator Agent
The Interview Question Generator creates interview questions using:
- Resume content
- Demonstrated competencies
- Demonstrated project concepts
- Job Description requirements

It generates:
- Technical Questions
- HR Questions
- Situational Questions

The questions progress from beginner to advanced based on the candidate's experience level.

## 6. APIs and Models Used
This project uses the **Gemini API** for all AI agent reasoning and text generation.

The API Key is securely managed using environment variables stored in a .env file, which is excluded from version control.

## 7. Retrieval Augmented Generation (RAG)
RAG and vector databases are not used in the current version of the project.

## 8. Streamlit Application Flow
1. Upload Resume (PDF)
2. Paste Job Description
3. Click Run Career Analysis
4. Execute Multi-Agent Pipeline
5. Display:
  * Skill Gap Analysis
  * Resume Optimization Suggestions
  * Interview Questions

## 9. Scoring Methodology
The Skill Comparator calculates four independent scores.

1. **Required Score**
Measures how well the candidate satisfies the mandatory skills and tools required by the Job Description.

2. **Preferred Score**
Measures alignment with optional or preferred skills and tools.

3. **Experience Relevance Score**
Measures how well the candidate's demonstrated professional competencies satisfy the experience expectations specified in the Job Description.

4. **Project Relevance Score**
Measures how well the candidate's projects demonstrate the technical concepts and technologies expected for the target role.

**Overall Resume Match Score**

The Overall Score is computed using weighted scoring:

- Required Score – 45%
- Preferred Score – 10%
- Experience Relevance Score – 15%
- Project Relevance Score – 30%

If one or more categories are not applicable for a given Job Description, their weights are automatically redistributed proportionally across the remaining applicable categories.

## 10. How to Run the Project
Step 1: Install Dependencies
pip install -r requirements.txt
Step 2: Run Streamlit App
streamlit run app.py

## 11. Project Output
The system generates:
- Resume–Job Matching Scores
- Skill Gap Analysis
- Resume Strengths
- Personalized Improvement Guidelines
- Resume Optimization Suggestions
- Technical Interview Questions
- HR Interview Questions
- Situational Interview Questions


**Author**
**Nivetha**
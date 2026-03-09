import autogen
from autogen import AssistantAgent
from utils import llm_config

#5. Interview question generating agent:
question_generator = AssistantAgent(
    name= 'question_generating_agent',
    llm_config=llm_config,
    system_message='''You are a helpful assistant. Your job is to generate interview questions based on users resume and job description.
    You will receive:
    1. Resume content
    2. Job Description
    Use this information to generate relevant interview questions.

    Return output as JSON format only:
    {
    'Technical questions':[],
    'HR questions':[],
    'Situation questions':[]
    }
    No need to provide answers. Each section (technical, HR and situation based questions) can contain 15 questions maximum, ranging from beginner level to            advanced level. If situation based questions section contains fewer questions, you may distribute additional questions to the other sections, if needed. 
    For freshers, you can provide questions from beginner to intermediate level. 
    For experienced, more advanced and project based questions can be provided. Likewise, think and produce questions analyzing the resume and JD thoroughly.
    Do not include explanations outside the JSON.'''
)
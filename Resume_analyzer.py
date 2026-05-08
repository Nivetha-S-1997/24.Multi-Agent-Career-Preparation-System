import autogen
from autogen import AssistantAgent
from utils import llm_config

#1. Resume Extracting agent:
resume_extractor = AssistantAgent(
    name= 'resume_extracting_agent',
    llm_config=llm_config,
    system_message='''You are a helpful assistant. Your job is to analyze the users resume and extract the information.
    Return the output ONLY in the following JSON format:
    {
    'Name':'',
    'Work experience':[],
    'Skills':[],
    'Tools':[],
    'Projects':[],
    'Education':[],
    'Certifications':[]
    }
    Do not rewrite or improve the content or optimize the resume or hallucinate. Just extract the contents.'''
)
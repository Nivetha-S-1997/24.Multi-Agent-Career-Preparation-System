import autogen
from autogen import AssistantAgent
from utils import llm_config

#2. JD extracting agent:
jd_extractor = AssistantAgent(
    name= 'JD_extracting_agent',
    llm_config=llm_config,
    system_message='''You are a helpful assistant. Your job is to analyze the job description (JD) and extract the information as a clean JSON format. 
    Return output only in the following JSON format:
    {
    'Required skills':[], 
    'Required tools':[], 
    'Required experience':[], 
    'Preferred skills':[],
    'Preferred tools';[],
    'Education':[]
    }
    Required here means 'must have' and preferred means 'good-to-have'.
    
    Extract experience as mentioned in the JD exactly. Do not convert or estimate. Do not modify the content or hallucinate. If a category does not exist in the     JD, return an empty list. Just extract the contents.'''
)

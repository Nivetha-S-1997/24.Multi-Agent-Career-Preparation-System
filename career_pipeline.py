from AI_agents.Resume_analyzer import resume_extractor
from AI_agents.JD_extractor import jd_extractor
from AI_agents.Skillgap_analyzer import skillgap_analyzer
from AI_agents.Resume_optimizer import resume_optimizer
from AI_agents.Question_generator import question_generator

#import utils
from utils import pdf_reader_func, string_to_dict

def run_career_pipeline(resume_text,jd_text):
    #Resume analyzer
    text=pdf_reader_func(resume_text)
    resume_reply = resume_extractor.generate_reply(messages = [{'content':text,'role':'user'}])
    resume_output=string_to_dict(resume_reply)
    
    #JD analyzer
    JD_reply = jd_extractor.generate_reply(messages = [{'content':jd_text,'role':'user'}])
    JD_output=string_to_dict(JD_reply)
    
    #Skill gap analyzer
    skillgap_input={
    'resume_skills':resume_output.get('Skills',[]),
    'resume_project':resume_output.get('Projects',[]),
    'resume_experience':resume_output.get('Work experience',[]),
    'jd_skills':JD_output.get('Required skills',[])
    }
    skill_analyzer_reply=skillgap_analyzer.generate_reply(messages=[{'role':'user','content':str(skillgap_input)}])
    skill_analyzer_output=string_to_dict(skill_analyzer_reply)
    
    #Resume optimizer
    optimizer_input = {
    'resume_data':resume_output,
    'JD_data':JD_output,
    'skillgap_data':skill_analyzer_output
    }
    optimizer_reply = resume_optimizer.generate_reply(messages=[{'role':'user','content':str(optimizer_input)}])
    optimizer_output=string_to_dict(optimizer_reply)
    
    #Interview question generator
    generator_input={
    'resume_data':resume_output,
    'JD_data':JD_output,
    }
    generator_reply = question_generator.generate_reply(messages=[{'role':'user','content':str(generator_input)}])
    generator_output=string_to_dict(generator_reply)

    return {
        "current_resume": text,
        "resume_analysis": resume_output,
        "jd_analysis": JD_output,
        "skill_gap_analysis": skill_analyzer_output,
        "optimized_resume": optimizer_output,
        "questions": generator_output
    }

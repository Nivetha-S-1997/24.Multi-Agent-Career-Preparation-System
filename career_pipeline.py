from AI_agents.Resume_analyzer import resume_extractor
from AI_agents.JD_extractor import jd_extractor
from AI_agents.Skillgap_analyzer import skillgap_analyzer
from AI_agents.Resume_optimizer import resume_optimizer
from AI_agents.Question_generator import question_generator
from utils import pdf_reader_func, string_to_dict

def run_career_pipeline(resume_text,jd_text):
    #Resume analyzer
    text = pdf_reader_func(resume_text)
    resume_reply = resume_extractor.generate_reply(messages = [{'role':'user','content':text}])
    resume_output = string_to_dict(resume_reply)
    print("\n========== RESUME ANALYZER OUTPUT ==========\n")
    print(resume_output)
    
    #JD analyzer
    JD_reply = jd_extractor.generate_reply(messages = [{'role':'user','content':jd_text}])
    JD_output = string_to_dict(JD_reply)
    print("\n========== JD ANALYZER OUTPUT ==========\n")
    print(JD_output)

    #Skill gap analyzer
    skillgap_input = {
    'resume_skills':resume_output.get('Skills',[]),
    'resume_tools':resume_output.get('Tools',[]),
    'resume_demonstrated_competencies': [
        competency
        for exp in resume_output.get('Work experience',[])
        for competency in exp.get('Demonstrated Competencies',[])
    ],
    'resume_demonstrated_concepts': [
        concept
        for project in resume_output.get('Projects',[])
        for concept in project.get('Demonstrated Concepts',[])
    ],
    'resume_project_technologies': [
        technology
        for project in resume_output.get('Projects',[])
        for technology in project.get('Technologies Used',[])
    ],
    
    'jd_required_skills':JD_output.get('Required skills',[]),
    'jd_required_tools':JD_output.get('Required tools',[]),
    'jd_preferred_skills':JD_output.get('Preferred skills',[]),
    'jd_preferred_tools':JD_output.get('Preferred tools',[]),
    'jd_experience_expectations':JD_output.get('Experience expectations',[]),
    'jd_project_expectations':JD_output.get('Project expectations',[])
    }
    skill_analyzer_reply = skillgap_analyzer.generate_reply(messages = [{'role':'user','content':str(skillgap_input)}])
    skill_analyzer_output = string_to_dict(skill_analyzer_reply)
    print("\n========== SKILL ANALYZER OUTPUT ==========\n")
    print(skill_analyzer_output)
    
    #Resume optimizer
    optimizer_input = {
    'resume_data':resume_output,
    'JD_data':JD_output,
    'skillgap_data':skill_analyzer_output
    }
    optimizer_reply = resume_optimizer.generate_reply(messages = [{'role':'user','content':str(optimizer_input)}])
    optimizer_output = string_to_dict(optimizer_reply)

    print("OPTIMIZER RAW REPLY:\n", optimizer_reply)
    print("OPTIMIZER PARSED OUTPUT:\n", optimizer_output)
    
    #Interview question generator
    generator_input = {
    'resume_data':resume_output,
    'JD_data':JD_output,
    }
    generator_reply = question_generator.generate_reply(messages = [{'role':'user','content':str(generator_input)}])
    generator_output = string_to_dict(generator_reply)

    return {
        'current_resume': text,
        'resume_analysis': resume_output,
        'jd_analysis': JD_output,
        'skill_gap_analysis': skill_analyzer_output,
        'optimized_resume': optimizer_output,
        'questions': generator_output
    }
import autogen
from autogen import AssistantAgent
from utils import llm_config

#4. Resume optimising agent:
resume_optimizer = AssistantAgent(
    name= 'resume_optimizing_agent',
    llm_config=llm_config,
    system_message = """You are a Resume Optimization Agent.
    Your task:
    1. Compare the resume content with the job description (JD).
    2. Identify ONLY the parts of the resume that should be improved to better match the JD.
    3. Return the output strictly in JSON format.
    
    IMPORTANT RULES:
    - Return ONLY JSON. No explanation text outside JSON.
    - Provide improvements as a list of changes.
    - Each change must include: section, original, improved, reason.
    - Do NOT rewrite the entire resume.
    - Do NOT include the full resume.
    - If nothing needs improvement, return an empty list for changes.
    
    Return output ONLY in this exact JSON format:
    {
      "changes": [
        {
          "section": "",
          "original": "",
          "improved": "",
          "reason": ""
        }
      ]
    }
    
    Possible section values: "Summary", "Skills", "Tools", "Projects", "Work Experience", "Education", "Certifications"."""
)
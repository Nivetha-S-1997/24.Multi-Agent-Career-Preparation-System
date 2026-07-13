import streamlit as st
from career_pipeline import run_career_pipeline

# Helper: Format optimized resume dict into readable text
def format_resume(data):

    # If already string, return
    if isinstance(data, str):
        return data

    # If not dict, convert to string
    if not isinstance(data, dict):
        return str(data)

    formatted = ""

    # If optimizer directly gave a clean text summary
    for key in data.keys():
        if "resume text" in key.lower():
            return str(data[key])

    # Otherwise handle structured sections
    for key, value in data.items():

        # Skip empty values
        if value is None or value == "" or value == []:
            continue

        formatted += f"\n\n=== {key.upper()} ===\n"

        # If value is plain string
        if isinstance(value, str):
            formatted += value + "\n"
            continue

        # If value is list
        if isinstance(value, list):

            for item in value:

                if isinstance(item, dict):

                    section = item.get("section", "").strip()
                    content = item.get("content", "")

                    # Skip empty section blocks
                    if section == "" and (content == "" or content == []):
                        continue

                    # If section missing but project_name exists
                    if section == "" and "project_name" in item:
                        section = "Projects"

                    # If still missing
                    if section == "":
                        section = "Details"

                    # Projects formatting
                    if section.lower() == "projects":
                        project_name = item.get("project_name", "Unnamed Project")
                        content_type = item.get("content_type", "")

                        formatted += f"\nPROJECT: {project_name}\n"

                        if content_type:
                            formatted += f"{content_type}:\n"

                        if isinstance(content, list):
                            for c in content:
                                formatted += f" - {c}\n"
                        else:
                            formatted += f" - {content}\n"

                    else:
                        formatted += f"\n{section.upper()}:\n"

                        if isinstance(content, list):
                            for c in content:
                                formatted += f" - {c}\n"
                        else:
                            formatted += f" - {content}\n"

                else:
                    formatted += f" - {item}\n"

        else:
            formatted += str(value) + "\n"

    # If formatting fails / becomes empty, fallback to raw dict string
    if formatted.strip() == "":
        return str(data)

    return formatted

# ---------- Page Setup ----------
st.set_page_config(
    page_title="AI Career Preparation System",
    page_icon="🤖",
    layout="wide"
)

# Dark theme CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b, #111827);
    color: #f8fafc !important;
}

html, body, [class*="css"] {
    color: #f8fafc !important;
}

h1, h2, h3, h4, h5, h6 {
    color: #38bdf8 !important;
    font-weight: 700;
}

p, span, div, li, label {
    color: #f8fafc !important;
    font-weight: 500;
}

section[data-testid="stSidebar"] {
    background-color: #111827 !important;
}

section[data-testid="stSidebar"] * {
    color: #f8fafc !important;
}

textarea, input {
    background-color: #1e293b !important;
    color: #f8fafc !important;
    border-radius: 10px;
    border: 1px solid #334155 !important;
}

.stButton > button {
    background-color: #38bdf8 !important;
    color: #0f172a !important;
    font-weight: bold;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
}

.stButton > button:hover {
    background-color: #0ea5e9 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- Session State ----------
if "result" not in st.session_state:
    st.session_state.result = None

# Title
st.title("🤖 Multi-Agent Career Preparation System")

# Sidebar workflow with arrows
st.sidebar.header("🔄 AI Agent Workflow")

st.sidebar.markdown("""
Resume → Resume Analyzer Agent  
JD → JD Analyzer Agent  
↓  
Skill Gap Comparator Agent  
↓  
Resume Optimizer Agent  
↓  
Interview Question Generator Agent
""")

# Inputs
st.subheader("📄 Upload Resume & Job Description")

col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

with col2:
    jd_text = st.text_area("Paste Job Description", height=200)

run_button = st.button("Run Career Analysis")

# Run Pipeline
if run_button:

    if resume_file is None or jd_text.strip() == "":
        st.warning("Please upload resume and paste job description.")
    else:

        st.subheader("⚙️ Agents Running Status")

        agent1 = st.empty()
        agent2 = st.empty()
        agent3 = st.empty()
        agent4 = st.empty()
        agent5 = st.empty()

        agent1.write("⏳ Resume Analyzer running...")
        agent2.write("⏳ JD Analyzer running...")
        agent3.write("⏳ Skill Gap Agent running...")
        agent4.write("⏳ Resume Optimizer running...")
        agent5.write("⏳ Interview Generator running...")

        with st.spinner("Running multi-agent pipeline..."):
            st.session_state.result = run_career_pipeline(resume_file, jd_text)

        agent1.write("✅ Resume Analyzer completed")
        agent2.write("✅ JD Analyzer completed")
        agent3.write("✅ Skill Gap Agent completed")
        agent4.write("✅ Resume Optimizer completed")
        agent5.write("✅ Interview Generator completed")

        st.success("Analysis Completed Successfully!")

# Display Results (Persistent)
if st.session_state.result is not None:

    result = st.session_state.result

    st.divider()

    st.subheader("📊 Skill Gap Analysis")
    st.markdown(result.get("skill_gap", result.get("skill_gap_analysis", "Not available")))

    st.divider()
    st.subheader("✨ Resume Optimization Suggestions")
    
    improvements = result.get("optimized_resume", {})
    
    changes = improvements.get("changes", [])
    
    if not changes:
        st.info("No major resume improvements required. Your resume matches the JD well.")
    else:
        for i, change in enumerate(changes, start=1):
            st.markdown(f"### Change {i}: {change.get('section', 'Unknown Section')}")
    
            st.markdown("**Original:**")
            st.write(change.get("original", ""))
    
            st.markdown("**Improved:**")
            st.write(change.get("improved", ""))
    
            st.markdown("**Reason:**")
            st.write(change.get("reason", ""))

            #if i < len(changes):
            #st.write("---")

    st.divider()

    st.subheader("💬 Interview Questions")
    st.markdown(result.get("questions", "Not available"))

    st.divider()
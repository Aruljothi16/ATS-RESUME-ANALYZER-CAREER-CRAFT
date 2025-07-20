from dotenv import load_dotenv
import streamlit as st
from streamlit_extras import add_vertical_space as avs
import google.generativeai as genai
import os
import PyPDF2
from PIL import Image

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash')  # fallback to available model if 2.5 isn't supported

# Function to get response from Gemini
def get_gemini_response(resume_text, jd_text):
    input_prompt = f"""
    As an experienced ATS (Applicant Tracking System), proficient in the technical domain encompassing Software Engineering, Data Science, Data Analysis, Big Data Engineering, Web Developer, Mobile App Developer, DevOps Engineer, Machine Learning Engineer, Cybersecurity Analyst, Cloud Solutions Architect, Database Administrator, Network Engineer, AI Engineer, Systems Analyst, Full Stack Developer, UI/UX Designer, IT Project Manager, and additional specialized areas, your objective is to meticulously assess resumes against provided job descriptions. In a fiercely competitive job market, your expertise is crucial in offering top-notch guidance for resume enhancement. Assign precise matching percentages based on the JD (Job Description) and meticulously identify any missing keywords with utmost accuracy.

    Resume: {resume_text}
    Description: {jd_text}

    I want the response in the following structure:
    The first line indicates the percentage match with the job description (JD).
    The second line presents a list of missing keywords.
    The third section provides a profile summary.
    Mention the title for all the three sections.

    While generating the response put some space to separate all the three sections.
    """
    response = model.generate_content(input_prompt)
    return response.text

# Function to extract text from uploaded PDF
def input_pdf_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

# Streamlit UI setup
st.set_page_config(page_title="Resume ATS Tracker", layout="wide")
avs.add_vertical_space(2)

# Title and Intro Section
col1, col2 = st.columns([3, 2])
with col1:
    st.title("CareerCraft")
    st.header("Navigate the Job Market with Confidence!")
    st.markdown("""<p style='text-align: justify;'>
    Introducing CareerCraft, an ATS-Optimized Resume Analyzer — your ultimate solution for optimizing job applications and accelerating career growth. Our innovative platform leverages advanced ATS technology to provide job seekers with valuable insights into their resume's compatibility with job descriptions. From resume optimization and skill enhancement to career progression guidance, CareerCraft empowers users to stand out in today's competitive job market. Streamline your job application process, enhance your skills, and navigate your career path with confidence. Join CareerCraft today and unlock new opportunities for professional success!
    </p>""", unsafe_allow_html=True)
with col2:
    st.image('https://cdn.dribbble.com/userupload/12500996/file/original-b458fe398a6d7f4e9999ce66ec856ff9.gif', use_container_width=True)

avs.add_vertical_space(4)

# Offerings Section
col1, col2 = st.columns([2, 3])
with col1:
    img1 = Image.open("image/i2.png")
    st.image(img1, use_container_width=True)
with col2:
    st.header("Wide Range of Offerings")
    st.write("- ATS-Optimized Resume Analysis")
    st.write("- Resume Optimization")
    st.write("- Skill Enhancement")
    st.write("- Career Progression Guidance")
    st.write("- Tailored Profile Summaries")
    st.write("- Streamlined Application Process")
    st.write("- Personalized Recommendations")
    st.write("- Efficient Career Navigation")

avs.add_vertical_space(4)

# Upload & Analyze Section
col1, col2 = st.columns([3, 2])
with col1:
    st.markdown("<h1 style='text-align: center;'>Embark on Your Career Adventure</h1>", unsafe_allow_html=True)
    jd = st.text_area("📋 Paste the Job Description here")
    uploaded_file = st.file_uploader("📎 Upload Your Resume (PDF only)", type="pdf", help="Please upload your resume as a PDF.")
    submit = st.button("🚀 Submit for Analysis")

    if submit:
        if uploaded_file is not None and jd.strip() != "":
            with st.spinner("Analyzing your resume..."):
                resume_text = input_pdf_text(uploaded_file)
                response = get_gemini_response(resume_text, jd)
                st.subheader("🎯 ATS Analysis Result")
                st.write(response)
        else:
            st.warning("⚠️ Please upload a resume and enter a job description.")
with col2:
    img2 = Image.open("image/icon6.jpg")
    st.image(img2, use_container_width=True)

avs.add_vertical_space(4)

# FAQ Section
col1, col2 = st.columns([2, 3])
with col1:
    img3 = Image.open("image/icon5.png")
    st.image(img3, use_container_width=True)
with col2:
    st.markdown("<h1 style='text-align: center;'>📚 FAQ</h1>", unsafe_allow_html=True)
    st.markdown("**Q: How does CareerCraft analyze resumes and job descriptions?**")
    st.markdown("A: CareerCraft uses advanced algorithms to analyze resumes and job descriptions, identifying key keywords and assessing compatibility between the two.")
    avs.add_vertical_space(1)

    st.markdown("**Q: Can CareerCraft suggest improvements for my resume?**")
    st.markdown("A: Yes, CareerCraft provides personalized recommendations to optimize your resume for specific job openings, including suggestions for missing keywords and alignment with desired job roles.")
    avs.add_vertical_space(1)

    st.markdown("**Q: Is CareerCraft suitable for both entry-level and experienced professionals?**")
    st.markdown("A: Absolutely! CareerCraft caters to job seekers at all career stages, offering tailored insights and guidance to enhance their resumes and advance their careers.")

avs.add_vertical_space(3)

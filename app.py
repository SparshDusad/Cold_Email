import streamlit as st
from core.scraper import fetch_html, extract_visible_text
from core.extractor import extract_job_info
from core.resume_parser import extract_resume_text_from_filelike, summarize_resume
from core.email_generator import generate_cold_email

st.set_page_config(page_title="Gemini Cold Email Generator", layout="centered")
st.title("AI-Powered Cold Email Generator")

job_url = st.text_input("Paste a job posting URL:")
resume_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

if st.button("Generate Cold Email"):
    if not job_url or not resume_file:
        st.error("Please provide both the job URL and resume.")
        st.stop()

    try:
        with st.spinner("Scraping job post..."):
            html = fetch_html(job_url)
            job_text = extract_visible_text(html)

        with st.spinner("🧠 Extracting structured job info using Gemini..."):
            job_info = extract_job_info(job_text)
            if "error" in job_info:
                st.error(" Failed to extract job info.")
                st.text(job_text[:1000])
                st.stop()
            st.success("✅ Job info extracted!")
            # st.json(job_info)

        with st.spinner("Reading resume..."):
            resume_text = extract_resume_text_from_filelike(resume_file)
            resume_summary = summarize_resume(resume_text)

        with st.spinner("Generating cold email..."):
            email = generate_cold_email(job_info, resume_summary)
            st.subheader(" Your Cold Email")
            st.text_area("Copy and send this:", email, height=300)

    except Exception as e:
        st.error(f"Unexpected error: {e}")

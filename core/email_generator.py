from langchain_google_genai import ChatGoogleGenerativeAI

def generate_cold_email(job_info: dict, resume_summary: str) -> str:
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

    prompt = f"""
You are a career coach. Write a personalized cold email for a job opening using the info below.

Job Info:
- Title: {job_info.get('job_title')}
- Company: {job_info.get('company')}
- Location: {job_info.get('location')}
- Type: {job_info.get('job_type')}
- Requirements:
{chr(10).join(['• ' + r for r in job_info.get('qualifications', [])])}

Resume Summary:
{resume_summary}

Make the email friendly, focused on fit, and end with a request for a quick call. Limit to 200 words.
"""

    return model.predict(prompt).strip()

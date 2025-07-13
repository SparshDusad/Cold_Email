from langchain_google_genai import ChatGoogleGenerativeAI
import json
import re

def extract_json_from_text(text: str) -> dict:
    try:
        json_str = re.search(r'\{.*\}', text, re.DOTALL).group(0)
        return json.loads(json_str)
    except:
        return {"error": "Failed to parse JSON from Gemini"}

def extract_job_info(job_text: str) -> dict:
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

    prompt = f"""
Extract the following fields from this job description in valid JSON only:

- job_title
- company
- location
- job_type
- responsibilities (as list)
- qualifications (as list)
- tech_stack (as list)
- posted_date

Job Post:
\"\"\"
{job_text}
\"\"\"
"""

    response = model.invoke(prompt)
    raw = response.content.strip()

    try:
        return json.loads(raw)
    except:
        return extract_json_from_text(raw)

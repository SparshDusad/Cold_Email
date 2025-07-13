import PyPDF2

def extract_resume_text_from_filelike(file) -> str:
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def summarize_resume(resume_text: str) -> str:
    return resume_text[:500].replace('\n', ' ').strip()

import requests
from bs4 import BeautifulSoup

def fetch_html(url: str) -> str:
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers, timeout=10)
    if resp.status_code != 200:
        raise Exception(f"Failed to fetch page. Status: {resp.status_code}")
    return resp.text

def extract_visible_text(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup(['script', 'style', 'footer', 'nav']):
        tag.decompose()
    return soup.get_text(separator=' ', strip=True)

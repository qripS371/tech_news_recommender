import yaml
import logging
from datetime import datetime
from bs4 import BeautifulSoup
import requests

def load_config():
    with open("config.yaml") as f:
        return yaml.safe_load(f)

def get_today():
    return datetime.now().strftime("%Y-%m-%d")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_text(url):
    try:
        resp = requests.get(url, timeout=10)
        soup = BeautifulSoup(resp.text, 'html.parser')
        text = ' '.join([p.text for p in soup.find_all('p')])
        return text[:2000]  # Truncate for embeddings
    except:
        return ""
from sentence_transformers import SentenceTransformer
from utils.helpers import extract_text

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_article(title, description, url):
    text = f"{title} {description} {extract_text(url)}"
    return model.encode(text)
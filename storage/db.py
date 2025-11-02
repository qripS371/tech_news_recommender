import sqlite3
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from utils.helpers import load_config, get_today, extract_text, logger

# Load the lightweight sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Database file
DB_NAME = "tech_prefs.db"


def init_db():
    """Create the preferences table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS prefs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE,
            title TEXT,
            text TEXT,
            embedding BLOB,
            added_date TEXT
        )
    ''')
    conn.commit()
    conn.close()


def add_preference(url, title=""):
    """
    Add or update a preferred article.
    - Extracts text from URL
    - Embeds it
    - Stores in SQLite
    """
    text = extract_text(url)  # Now imported correctly
    embedding = model.encode(text).tobytes()

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT OR REPLACE INTO prefs (url, title, text, embedding, added_date)
        VALUES (?, ?, ?, ?, ?)
    ''', (url, title, text, embedding, get_today()))
    conn.commit()
    conn.close()

    logger.info(f"Added preference: {url}")


def get_preferences():
    """
    Retrieve all stored embeddings as a NumPy array.
    Returns a neutral random vector if none exist.
    """
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT embedding FROM prefs")
    rows = c.fetchall()
    conn.close()

    if not rows:
        return np.random.rand(1, 384)  # Fallback neutral vector

    embeddings = [np.frombuffer(row[0], dtype=np.float32) for row in rows]
    return np.array(embeddings)


def get_all_prefs():
    """Return full table as pandas DataFrame (for debugging/export)."""
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM prefs", conn)
    conn.close()
    return df
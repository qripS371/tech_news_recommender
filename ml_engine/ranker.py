import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from storage.db import get_preferences
from ml_engine.embedder import embed_article

def rank_articles(df):
    prefs_emb = get_preferences()
    if len(prefs_emb) == 0:
        return df.head(5)  # Default top by recency if no prefs
    
    scores = []
    for idx, row in df.iterrows():
        art_emb = embed_article(row['title'], row['description'], row['url'])
        sim = cosine_similarity([art_emb], prefs_emb)[0].max()  # Max sim to any pref
        scores.append(sim)
    
    df['score'] = scores
    return df.sort_values('score', ascending=False).head(5)
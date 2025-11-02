import re
import pandas as pd
from utils.helpers import load_config

# Load config once at import time
config = load_config()

def filter_tech(df):
    all_kws = (config['keywords']['tech_general'] +
               config['keywords']['ai'] +
               config['keywords']['hardware'] +
               config['keywords']['companies'])
    pattern = '|'.join([kw.lower() for kw in all_kws])
    df['relevance'] = df['title'].apply(
        lambda t: len(re.findall(pattern, str(t).lower())) if pd.notna(t) else 0
    )
    return df[df['relevance'] > 0].sort_values('relevance', ascending=False).head(20)
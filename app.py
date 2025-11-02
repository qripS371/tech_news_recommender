import streamlit as st
import pandas as pd
from fetcher.news_fetcher import fetch_articles, fetch_papers
from fetcher.filter import filter_tech
from ml_engine.ranker import rank_articles
from storage.db import init_db, add_preference, get_all_prefs
from utils.helpers import extract_text

# Page config
st.set_page_config(page_title="Tech News Curator", layout="wide")
st.title("Your Personal AI Tech Curator")
st.caption("Top 5 AI, Hardware & Company News — Personalized by You")

# Initialize
init_db()

# Sidebar: Add Preference
with st.sidebar:
    st.header("Add a Preference")
    url = st.text_input("Article URL")
    title = st.text_input("Title (optional)")
    if st.button("Add & Train Model"):
        if url:
            with st.spinner("Extracting & embedding..."):
                add_preference(url, title or "Untitled")
            st.success("Added! Model updated.")
        else:
            st.error("Enter a URL")

    st.divider()
    st.header("Your Preferences")
    prefs = get_all_prefs()
    if not prefs.empty:
        for _, row in prefs.iterrows():
            st.markdown(f"**{row['title'] or 'Untitled'}**")
            st.caption(f"[{row['url']}]({row['url']})")
    else:
        st.info("No preferences yet.")

# Main: Fetch & Rank
if st.button("Fetch Today's Top 5", type="primary"):
    with st.spinner("Fetching & ranking..."):
        articles = fetch_articles()
        papers = fetch_papers()
        all_news = pd.concat([articles, papers], ignore_index=True) if not articles.empty and not papers.empty else articles if not articles.empty else papers

        if all_news.empty:
            st.warning("No news today. Try again later or add preferences.")
        else:
            filtered = filter_tech(all_news)
            top5 = rank_articles(filtered)

            for i, row in top5.iterrows():
                score = getattr(row, 'score', 'N/A')
                with st.container():
                    col1, col2 = st.columns([4, 1])
                    with col1:
                        st.markdown(f"#### {i+1}. **{row['title']}**")
                        st.caption(row['description'][:200] + '...')
                        st.markdown(f"[Read more]({row['url']})")
                    with col2:
                        st.metric("Score", f"{score:.2f}")
                    st.divider()
else:
    st.info("Click **Fetch Today's Top 5** to start.")

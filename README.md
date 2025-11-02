# Personal AI Tech News Curator

![Tech News](https://img.shields.io/badge/Tech-AI%20News-brightgreen)

A smart ML-powered butler that fetches daily top 5 tech stories (AI, Nvidia, OpenAI, hardware, papers) from NewsAPI & arXiv, ranks them by your preferences, and learns as you add links.

## Features
- **Daily Fetch**: Top 5 personalized news
- **ML Ranking**: Sentence embeddings + cosine similarity
- **Train It**: Add links → it remembers your taste
- **CLI**: python main.py fetch
- **Web UI**: streamlit run app.py

## Setup
1. pip install -r requirements.txt
2. Add your NewsAPI key to config.yaml
3. python main.py fetch

## Usage
- Add pref: python main.py add <url> --title "Title"
- Fetch: python main.py fetch
- UI: streamlit run app.py

Built with ❤️ using sentence-transformers, NewsAPI, arXiv.

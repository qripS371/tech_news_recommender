# Personal AI Tech News Curator

![Tech News](https://img.shields.io/badge/Tech-AI%20News-brightgreen)

A smart ML-powered butler that fetches daily top 5 tech stories (AI, Nvidia, OpenAI, hardware, papers) from NewsAPI & arXiv, ranks them by your preferences, and learns as you add links.
We've built a smart personal tech news butler that scours the internet every day for the hottest stories on AI breakthroughs, Nvidia GPUs, OpenAI updates, hardware innovations, and cutting-edge research papers. It fetches fresh articles and papers, filters out the noise, and—here’s the magic—lets **you** shape its brain: every time you spot a gem and add its link, it quietly stores your preference, trains its machine learning model to understand *your* exact taste in tech, and remembers forever. The more you feed it, the smarter it gets, so it uses that growing personal wisdom to rank the top 5 just for you. Run it from the command line for a quick list or open the web dashboard to click, browse, and add preferences with zero hassle.

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

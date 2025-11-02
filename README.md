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
Below is a complete, copy-paste-ready README.md you can add to your GitHub repo:
markdown# Tech News Recommender  
**Your personal AI-powered daily tech news curator** – fetches top 5 stories (AI, Nvidia, OpenAI, hardware, arXiv papers), ranks them by your taste, and learns as you add favorites.

Live Demo: [https://tech-news-recommender-qrips371.streamlit.app](https://tech-news-recommender-qrips371.streamlit.app)  
GitHub: [qripS371/tech_news_recommender](https://github.com/qripS371/tech_news_recommender)

---

## How to Run Locally (Windows / macOS / Linux)

### 1. **Clone the Repo**
```bash
git clone https://github.com/qripS371/tech_news_recommender.git
cd tech_news_recommender
2. (Recommended) Create a Virtual Environment
bashpython -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
3. Install Dependencies
bashpip install -r requirements.txt

Includes: streamlit, pandas, sentence-transformers, newsapi-python, arxiv, etc.

4. Get a Free NewsAPI Key

Go to: https://newsapi.org/register
Create free account → Copy your API key

5. Set Your API Key
Create a file .streamlit/secrets.toml in the project root:
tomlNEWSAPI_KEY = "your_actual_key_here"

Never commit this file — it's in .gitignore.

6. Run the App
bashstreamlit run app.py
Opens in browser: http://localhost:8501

Features

Fetch Top 5 daily tech news (AI, GPUs, Nvidia, OpenAI, research papers)
Add Preferences → trains ML model (sentence embeddings + cosine similarity)
Web UI (Streamlit) + CLI support
No heavy training — lightweight, learns on-the-fly


Project Structure
texttech_news_recommender/
├── app.py                  # Streamlit dashboard
├── requirements.txt
├── .gitignore
├── fetcher/                # NewsAPI + arXiv fetchers
├── ml_engine/              # Embedding + ranking
├── storage/                # SQLite preferences
└── utils/                  # Helpers + text extraction

Troubleshooting

























IssueFixModuleNotFoundErrorRun pip install -r requirements.txt againNEWSAPI_KEY errorAdd key to .streamlit/secrets.tomlSlow first loadsentence-transformers downloads ~150MB modelNo news?Free NewsAPI: 100 calls/day. Try adding preferences.

Deploy Your Own Live Version

Fork this repo
Go to share.streamlit.io
New App → Connect your fork → app.py
Add NEWSAPI_KEY in Secrets
Deploy → Get your own live URL!


Built with Streamlit, Sentence Transformers, NewsAPI, arXiv
License: MIT
text---

### How to Add This to Your Repo (One-Time)

In **PowerShell** (from `D:\tech_news_recommender`):

```powershell
@"
# Tech News Recommender  
**Your personal AI-powered daily tech news curator** – fetches top 5 stories (AI, Nvidia, OpenAI, hardware, arXiv papers), ranks them by your taste, and learns as you add favorites.

Live Demo: [https://tech-news-recommender-qrips371.streamlit.app](https://tech-news-recommender-qrips371.streamlit.app)  
GitHub: [qripS371/tech_news_recommender](https://github.com/qripS371/tech_news_recommender)

---

## How to Run Locally (Windows / macOS / Linux)

### 1. **Clone the Repo**
```bash
git clone https://github.com/qripS371/tech_news_recommender.git
cd tech_news_recommender
2. (Recommended) Create a Virtual Environment
bashpython -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
3. Install Dependencies
bashpip install -r requirements.txt

Includes: streamlit, pandas, sentence-transformers, newsapi-python, arxiv, etc.

4. Get a Free NewsAPI Key

Go to: https://newsapi.org/register
Create free account → Copy your API key

5. Set Your API Key
Create a file .streamlit/secrets.toml in the project root:
tomlNEWSAPI_KEY = "your_actual_key_here"

Never commit this file — it's in .gitignore.

6. Run the App
bashstreamlit run app.py
Opens in browser: http://localhost:8501

Features

Fetch Top 5 daily tech news (AI, GPUs, Nvidia, OpenAI, research papers)
Add Preferences → trains ML model (sentence embeddings + cosine similarity)
Web UI (Streamlit) + CLI support
No heavy training — lightweight, learns on-the-fly


Project Structure
texttech_news_recommender/
├── app.py                  # Streamlit dashboard
├── requirements.txt
├── .gitignore
├── fetcher/                # NewsAPI + arXiv fetchers
├── ml_engine/              # Embedding + ranking
├── storage/                # SQLite preferences
└── utils/                  # Helpers + text extraction

Troubleshooting

























IssueFixModuleNotFoundErrorRun pip install -r requirements.txt againNEWSAPI_KEY errorAdd key to .streamlit/secrets.tomlSlow first loadsentence-transformers downloads ~150MB modelNo news?Free NewsAPI: 100 calls/day. Try adding preferences.

Deploy Your Own Live Version

Fork this repo
Go to share.streamlit.io
New App → Connect your fork → app.py
Add NEWSAPI_KEY in Secrets
Deploy → Get your own live URL!


Built with Streamlit, Sentence Transformers, NewsAPI, arXiv
License: MIT
"@ | Out-File -FilePath README.md -Encoding UTF8
git add README.md
git commit -m "Add complete installation guide"
git push origin main
text---

**Done!**  
Anyone who downloads your repo will:
1. Clone
2. `pip install -r requirements.txt`
3. Add their **NewsAPI key**
4. `streamlit run app.py`

**Zero confusion. Works on any machine.**

Want a **PDF version** or **video tutorial**? Say the word.

## Usage
- Add pref: python main.py add <url> --title "Title"
- Fetch: python main.py fetch
- UI: streamlit run app.py

Built with ❤️ using sentence-transformers, NewsAPI, arXiv.

from newsapi import NewsApiClient
import arxiv
import pandas as pd
from utils.helpers import load_config, get_today, logger

config = load_config()
newsapi = NewsApiClient(api_key=config['newsapi_key'])

def fetch_articles():
    """Fetch news articles with robust error handling."""
    kw = ' OR '.join(config['keywords']['ai'] + config['keywords']['hardware'] + config['keywords']['companies'])
    try:
        data = newsapi.get_everything(
            q=kw,
            from_param=get_today(),
            language='en',
            sort_by='publishedAt',
            page_size=50
        )
        articles = data.get('articles', [])
        if not articles:
            logger.warning("No articles from NewsAPI.")
            return pd.DataFrame(columns=['title', 'url', 'description', 'publishedAt'])

        df = pd.DataFrame(articles)
        for col in ['title', 'url', 'description', 'publishedAt']:
            if col not in df.columns:
                df[col] = ""

        domains = '|'.join(config['sources']['news_domains'])
        mask = df['url'].str.contains(domains, na=False, case=False)
        filtered = df[mask]
        if filtered.empty:
            logger.info("No trusted domains. Using all.")
            filtered = df
        return filtered[['title', 'url', 'description', 'publishedAt']].head(20)

    except Exception as e:
        logger.error(f"NewsAPI error: {e}")
        return pd.DataFrame(columns=['title', 'url', 'description', 'publishedAt'])

def fetch_papers():
    """Fetch arXiv papers safely."""
    try:
        # Narrow query to avoid crash
        query = ' OR '.join(config['keywords']['ai'][:3]) + " AND (research OR paper)"
        search = arxiv.Search(query=query, max_results=20)
        results = []
        for r in search.results():
            results.append({
                'title': r.title,
                'url': r.entry_id,
                'description': r.summary[:200],
                'publishedAt': r.published.date().isoformat()
            })
        return pd.DataFrame(results)
    except Exception as e:
        logger.error(f"arXiv error: {e}")
        return pd.DataFrame()
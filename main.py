import click
import pandas as pd
from fetcher.news_fetcher import fetch_articles, fetch_papers
from fetcher.filter import filter_tech
from ml_engine.ranker import rank_articles
from storage.db import init_db, add_preference

@click.group()
def cli():
    init_db()
    pass

@cli.command()
@click.argument('url')
@click.option('--title', default='')
def add(url, title):
    """Add a preferred tech news link to train preferences."""
    add_preference(url, title)
    click.echo(f"Added: {url}")

@cli.command()
def fetch():
    """Fetch and show top 5 tech news of the day."""
    # Fetch
    articles = fetch_articles()
    papers = fetch_papers()
    all_news = pd.concat([articles, papers], ignore_index=True)
    
    # Filter & Rank
    filtered = filter_tech(all_news)
    top5 = rank_articles(filtered)
    
    # Output
    for idx, row in top5.iterrows():
        score = getattr(row, 'score', 'N/A')
        click.echo(f"\n{idx+1}. **{row['title']}** (Score: {score:.2f})")
        click.echo(f"   {row['description'][:100]}...")
        click.echo(f"   Link: {row['url']}")
        click.echo(f"   Date: {row['publishedAt']}")

if __name__ == '__main__':
    cli()
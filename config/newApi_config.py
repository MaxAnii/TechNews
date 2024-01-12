from newsapi import NewsApiClient
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("NEWSAPI_KEY")
newsapi = NewsApiClient(api_key=api_key)
search_query = os.getenv("TECH_KEY_WORDS")

def get_news():
    data = newsapi.get_everything(q=search_query,
                                        page_size=5,
                                          language='en',
                                          sort_by='publishedAt',
                                          page=1
                                          )
    return data

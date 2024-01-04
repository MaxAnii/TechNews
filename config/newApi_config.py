from newsapi import NewsApiClient
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("NEWSAPI_KEY")
# Init
newsapi = NewsApiClient(api_key=api_key)

# /v2/top-headlines
data = newsapi.get_everything(q='technology',
                                       to='2024-01-04',
                                      language='en',
                                      page=1,
                                      sort_by="popularity",
                                      page_size=3
                                       )
articles = data['articles']



from newsapi import NewsApiClient
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("NEWSAPI_KEY")
newsapi = NewsApiClient(api_key=api_key)


def get_news():
    data = newsapi.get_everything(q='technology OR coding OR programing OR software OR ai OR pyhton OR java OR javaScript OR reactjs OR software developer',
                                        page_size=5,
                                          language='en',
                                          sort_by='publishedAt',
                                          page=1
                                          )
    return data

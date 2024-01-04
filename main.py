from config.tweepy_config import client
from config.newApi_config import articles


for article in articles:
    source = article['source']
    author = article['author']
    title = article['title']
    description = article['description']
    url = article['url']
    urlToImage = article['urlToImage']
    publishedAt = article['publishedAt']
    content = article['content']
    tweet_text = f"Title: {title} \nSource: {source['name']}\n Author: {author} \n  URL: {url} \n Published At: {publishedAt}"
    client.create_tweet(text=tweet_text)




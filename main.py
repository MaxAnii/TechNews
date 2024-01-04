from config.tweepy_config import client
from config.newApi_config import get_news

data = get_news()
articles = data['articles']
print()
for article in articles:
    source = article['source']
    author = article['author']
    title = article['title']
    url = article['url']
    
    publishedAt = article['publishedAt']
    
    tweet_text = f"{title}\nSource: {source['name']}\nAuthor: {author}\nRead full article: {url}\n@technology @ai"
    if len(tweet_text) > 200:
        pass
    else:
        client.create_tweet(text=tweet_text)




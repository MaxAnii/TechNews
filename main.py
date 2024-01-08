import schedule
import time
from flask import Flask
from threading import Thread
from config.tweepy_config import client
from config.newApi_config import get_news

app = Flask(__name__)

def tweet():
    try:
        data = get_news()
        articles = data['articles']
        for article in articles:
            source = article['source']
            author = article['author']
            title = article['title']
            url = article['url']
            tweet_text = f"{title}\nSource: {source['name']}\nURL: {url}\n@technology @ai"
            if len(tweet_text) > 280:
                print(f"Skipping tweet: exceeds 250 characters ({len(tweet_text)} characters)")
            else:
                print(tweet_text)
                time.sleep(2)
                client.create_tweet(text=tweet_text)
    except:
        print("Error in Tweeting")

@app.route('/') 
def home():
    return 'Server is running!'

def schedule_tweet_function(request):
    schedule.every(3).minutes.do(tweet)
    while True:
        schedule.run_pending()
        time.sleep(1)


schedule_tweet_function(None)

if __name__ == '__main__':
    app.run()

import threading
import schedule
import time
from flask import Flask
from config.tweepy_config import client
from config.newApi_config import get_news

app = Flask(__name__)

def tweet():
    try:
        data = get_news()
        articles = data['articles']
        for article in articles:
            source = article['source']
            title = article['title']
            url = article['url']
            tweet_text = f"{title}\nSource: {source['name']}\nURL: {url}\n@technology @ai"
            if len(tweet_text) > 280:
                print(f"Skipping tweet: exceeds 280 characters ({len(tweet_text)} characters)")
            else:
                print(tweet_text)
                time.sleep(2)
                client.create_tweet(text=tweet_text)
    except Exception as error:
        print(error)

def schedule_tweet():
    schedule.every(3).hours.do(tweet)
    while True:
        schedule.run_pending()
        time.sleep(5)

@app.route('/')
def home():
    return 'Server is running!'

if __name__ == '__main__':
    thread = threading.Thread(target=schedule_tweet)
    thread.start()
    app.run()

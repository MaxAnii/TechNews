from flask import Flask
import schedule
import time
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
        
def schedule_tweet():
    # schedule.every().day.at("17:13").do(tweet)
    schedule.every(3).minutes.do(tweet)
def run_flask():
    app.run(debug=True)
    
if __name__ == '__main__':
    schedule_tweet() 
    print("testing log")
    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    while True:
        schedule.run_pending()
        time.sleep(1)

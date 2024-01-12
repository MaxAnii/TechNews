# TechNewsBot - Automated Technology News Tweets
TechNewsBot is a Python-based Twitter bot designed to automate tweets related to the latest technology news. The bot utilizes the News API to fetch real-time technology news articles and the Tweepy library to automate the tweeting process. This project aims to provide a convenient way to keep followers updated on the latest happenings in the tech world.

---
## Features
**Automated Tweets:** The bot automatically generates and tweets the latest technology news articles.

**Customizable Schedule:** You can configure the bot to tweet at specific intervals based on your preferences.

**NewsAPI Integration:**  Utilizes the News API to fetch a diverse range of technology news from various sources.  

---

## Getting Started
### Clone the Repository
```bash
git clone https://github.com/MaxAnii/Tweet_EveryDay.git
```
### Install Dependencies
```bash
pip install -r requirements.txt
```
### Configure API Keys
Obtain API keys for both the News API and Twitter API.

Create a `.env` file in the project root and add your API keys:
```env
API_KEY = your_twitter_api_key
API_KEY_SECRET = your_twitter_api_secret
ACCESS_TOKEN = your_twitter_access_token
ACCESS_TOKEN_SECRET = your_twitter_access_secret
NEWSAPI_KEY =your_news_api_key
TECH_KEY_WORDS = search query or key words
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
---
By [Ansar](https://github.com/MaxAnii) with ❤️.
Happy tweeting! 🐦✨

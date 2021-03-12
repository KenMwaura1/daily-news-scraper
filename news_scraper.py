import os
import time
import newspaper
import africastalking as at
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('api_key')
username = os.getenv('username')
mobile_number = os.getenv('mobile_number')

at.initialize(username, api_key)
sms = at.SMS

business_daily = "https://www.businessdailyafrica.com/"
standard_daily = "https://www.standardmedia.co.ke/"

message = []


def top_news(url):
    # get top articles on standard standard
    news_source = newspaper.build(url, memoize_articles=False)
    top_articles = []
    for index in range(3):
        article = news_source.articles[index]
        article.download()
        article.parse()
        top_articles.append(article)
    for a in top_articles:
        print(a.title, a.url)
        message.append(a.title)
        message.append(a.url)


top_news(business_daily)
top_news(standard_daily)

print(message)


def send_message(news: list, number: int):
    sms.send(news, [number])


send_message(str(message), mobile_number)

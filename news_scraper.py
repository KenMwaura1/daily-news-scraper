import os
import time
import newspaper
import africastalking as at


# get the environment values from the .env file
api_key = os.environ.get('api_key')
username = os.environ.get('username')
mobile_number = os.environ.get('mobile_number')
# Initialize the Africas talking client using username and api api_key
at.initialize(username, api_key)
# create a variable to reference the SMS client
sms = at.SMS

# create variables to hold urls to be scraped
business_daily = "https://www.businessdailyafrica.com/"
standard_daily = "https://www.standardmedia.co.ke/"
# create an empty list to hold the headlines and urls
message = []


# Create a function to scrape the top 3 headlines from news sources
def top_news(url):
    # get top articles on standard standard
    news_source = newspaper.build(url)
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


# Create a function to send a message containing the scraped news headlines.
def send_message(news: list, number: int):
    try:
        response = sms.send(news, [number])
        print(response)
    except Exception as e:
        print(f" Houston we have a problem: {e}")


# Call the function passing the message  and mobile_number as a arguments
send_message(str(message), mobile_number)

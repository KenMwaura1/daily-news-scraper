import os
import newspaper
import africastalking as at
import bitlyshortener as bts
from dotenv import load_dotenv

load_dotenv()

# get the environment values from the .env file
api_key = os.getenv('api_key')
username = os.getenv('username')
mobile_number = os.getenv('mobile_number')
# Initialize the Africas talking client using username and api_key
at.initialize(username, api_key)
# create a variable to reference the SMS client
sms = at.SMS
# Get the token(s) and create a shortener variable
token = os.getenv('bitly_token')
# create a variable to takes the token and returns a shortener object
shortener = bts.Shortener(tokens=[token], max_cache_size=256)

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
        # Shorten the long article urls using bitly shortener lib
        short_url = shortener.shorten_urls([a.url])
        message.append(a.title)
        # Short url is a list and we need to unpack it
        for url in short_url:
            message.append(url)


top_news(business_daily)
top_news(standard_daily)

print(message)
# Returns a the current usage of the url shortening quota
usage = shortener.usage()
print(f"Current url quota usage: {usage * 1000}%")


# Create a function to send a message containing the scraped news headlines.
def send_message(news: list, number: int):
    try:
        response = sms.send(news, [number])
        print(response)
    except Exception as e:
        print(f" Houston we have a problem: {e}")


# Call the function passing the message  and mobile_number as a arguments
send_message(str(message), mobile_number)

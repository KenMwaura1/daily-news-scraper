from newspaper import Article
import newspaper
import africastalking as at
from dotenv import load_dotenv

business_daily = "https://www.businessdailyafrica.com/"
standard_daily = "https://www.standardmedia.co.ke/"

message = []


def top_news(url):
    # get top articles on standard standard
    news_source = newspaper.build(url, memoize_articles=False)
    top_articles = []
    for index in range(5):
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

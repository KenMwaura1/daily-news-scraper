from newspaper import Article
import newspaper

""" 
url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
url2 = "https://nation.africa/kenya"
article = Article(url2)
article.download()
article.parse()
print(article.text)
print(article.text)
"""
bdaily = newspaper.build("https://www.businessdailyafrica.com/bd/corporate/technology", memoize_articles=False)
daily_nation = newspaper.build("https://nation.africa/kenya/news/tech", memoize_articles=False)
sdaily = newspaper.build("https://www.standardmedia.co.ke/", memoize_articles=False)


def top_news(url):
    # get top articles on standard standard
    news_source = newspaper.build(url,memoize_articles=False)
    top_articles = []
    for index in range(5):
        article = news_source.articles[index]
        article.download()
        article.parse()
        top_articles.append(article)
    for a in top_articles:
        print(a.title, a.url)


sample = bdaily.articles[2]
sample.download()
sample.parse()
print(sample.title)
print(sample.url)

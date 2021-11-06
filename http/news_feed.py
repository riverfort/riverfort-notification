import feedparser


def get_recent_news(company_symbol):
    uk_news_feed_url = "https://www.investegate.co.uk/Rss.aspx?company="
    news_feed = feedparser.parse(uk_news_feed_url + company_symbol)
    result = news_feed["entries"][0]
    return result


print(get_recent_news("RMM"))

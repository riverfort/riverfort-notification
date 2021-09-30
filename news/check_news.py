from database.configuration.config import DatabaseConnection


database = DatabaseConnection(
    "riverfort_notification", "riverfort", "rgctechnology", "localhost", 5432
)

uk_news_url = "https://www.investegate.co.uk/Rss.aspx?company="

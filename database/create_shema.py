from database.config.config import DatabaseConnection


database = DatabaseConnection(
    "riverfort_notification", "riverfort", "rgctechnology", "localhost", 5432
)

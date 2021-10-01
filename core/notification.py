from db_config.connection import DatabaseConnection

database = DatabaseConnection(
    "riverfort_notification", "riverfort", "rgctechnology", "localhost", 5432
)


def send_push_notification():
    device_tokens = fetch_all_device_tokens_of("RMM")
    for device_token in device_tokens:
        print("Send Push Notification to: " + device_token)


def fetch_all_device_tokens_of(company_symbol):
    device_tokens = database.filter_data(
        "SELECT device_token FROM watchlist WHERE company_symbol=%s", (company_symbol,)
    )
    return [i[0] for i in device_tokens]


send_push_notification()

import requests


class CompanyQuote:
    def __init__(self, company_symbol, price, change, change_percent):
        super().__init__()
        self.company_symbol = company_symbol
        self.price = price
        self.change = change
        self.change_percent = change_percent

    def __str__(self):
        return f"""CompanyQuote: 
        - company_symbol: {self.company_symbol}
        - price: {self.price}
        - change: {self.change}
        - change_percent: {self.change_percent}
        """


def get_companys_quote(symbols):
    payload = {"symbols": ",".join(symbols)}
    r = requests.get(
        f"https://query2.finance.yahoo.com/v7/finance/quote",
        params=payload,
        headers={"User-agent": "Mozilla/5.0"},
    )
    quotes = r.json()["quoteResponse"]["result"]
    result = []
    for quote in quotes:
        companyQuote = CompanyQuote(
            company_symbol=quote["symbol"].split(".")[0],
            price=quote["regularMarketPrice"],
            change=quote["regularMarketChange"],
            change_percent=quote["regularMarketChangePercent"],
        )
        result.append(companyQuote)
    return result


result = get_companys_quote([""])
for r in result:
    print(r)

import requests
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from models.company_quote import CompanyQuote


def get_company_quote(symbol: str) -> CompanyQuote:
    payload = {"modules": "price"}
    r = requests.get(
        f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{symbol}",
        params=payload,
        headers={"User-agent": "Mozilla/5.0"},
    )
    result = r.json()["quoteSummary"]["result"]
    if result is not None and result:
        price_module = result[0]["price"]

        if (
            "regularMarketPrice" in price_module
            and "fmt" in price_module["regularMarketPrice"]
        ):
            fmt_price = price_module["regularMarketPrice"]["fmt"]
        else:
            fmt_price = None

        if (
            "regularMarketChange" in price_module
            and "fmt" in price_module["regularMarketChange"]
        ):
            fmt_change = price_module["regularMarketChange"]["fmt"]
        else:
            fmt_change = None

        if (
            "regularMarketChangePercent" in price_module
            and "fmt" in price_module["regularMarketChangePercent"]
        ):
            fmt_change_percent = price_module["regularMarketChangePercent"]["fmt"]
        else:
            fmt_change_percent = None

        companyQuote = CompanyQuote(
            company_symbol=symbol,
            price=fmt_price,
            change=fmt_change,
            change_percent=fmt_change_percent,
        )
        return companyQuote

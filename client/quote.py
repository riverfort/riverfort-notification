import requests
import traceback
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
    try:
        result = r.json()["quoteSummary"]["result"]
        if result is not None and result:
            price_module = result[0]["price"]

            if (
                "regularMarketPrice" in price_module
                and "raw" in price_module["regularMarketPrice"]
            ):
                raw_price = price_module["regularMarketPrice"]["raw"]
            else:
                raw_price = None

            if (
                "regularMarketChange" in price_module
                and "raw" in price_module["regularMarketChange"]
            ):
                raw_change = price_module["regularMarketChange"]["raw"]
            else:
                raw_change = None

            if (
                "regularMarketChangePercent" in price_module
                and "raw" in price_module["regularMarketChangePercent"]
            ):
                raw_change_percent = price_module["regularMarketChangePercent"]["raw"]
            else:
                raw_change_percent = None

            if "regularMarketTime" in price_module:
                market_time = price_module["regularMarketTime"]
            else:
                market_time = None

            companyQuote = CompanyQuote(
                company_symbol=symbol,
                price=raw_price,
                change=raw_change,
                change_percent=raw_change_percent,
                market_time=market_time,
            )
            return companyQuote
    except Exception:
        print(f"ERROR: get company quote: {symbol}")
        traceback.print_exc()
        return

import requests
import os
import sys
import inspect
from typing import List

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from models.company_quote import CompanyQuote


def get_companys_quote(symbols: List[str]) -> List[CompanyQuote]:
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

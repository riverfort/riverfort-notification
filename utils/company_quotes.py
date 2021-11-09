import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from models.company_quote import CompanyQuote


def get_top_gain_company_quotes(conn) -> CompanyQuote:
    company_quotes = conn.get(
        "SELECT * FROM company_quotes WHERE change_percent IS NOT NULL ORDER BY change_percent DESC LIMIT 30"
    )
    result = list(
        map(
            lambda company_quote: CompanyQuote(
                company_symbol=company_quote[0],
                price=company_quote[1],
                change=company_quote[2],
                change_percent=company_quote[3],
            ),
            company_quotes,
        )
    )
    return result

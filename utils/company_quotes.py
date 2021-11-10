import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from models.company_quote import CompanyQuote


def get_top_gain_company_quotes(conn) -> CompanyQuote:
    company_quotes = conn.get(
        """
        SELECT CQS.company_symbol, price, change, change_percent, market_time
        FROM company_quotes CQS INNER JOIN companies CS ON CQS.company_symbol=CS.company_symbol
        WHERE change_percent IS NOT NULL ORDER BY change_percent DESC LIMIT 100
        """
    )
    result = list(
        map(
            lambda company_quote: CompanyQuote(
                company_symbol=company_quote[0],
                price=company_quote[1],
                change=company_quote[2],
                change_percent=company_quote[3],
                market_time=company_quote[4],
            ),
            company_quotes,
        )
    )
    return result

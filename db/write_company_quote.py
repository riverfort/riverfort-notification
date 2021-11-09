import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from db.conn import Conn
from client.quote import get_company_quote
import utils.companies as companies

conn = Conn(
    host="localhost",
    port=5432,
    database="riverfort_notification",
    user="riverfort",
    password="rgctechnology",
)

company_symbols = companies.get_company_symbols(conn=conn)
company_symbols_fmt = list(
    map(lambda company_symbol: f"{company_symbol}.L", company_symbols)
)

for symbol in company_symbols_fmt:
    companyQuote = get_company_quote(symbol=symbol)
    if companyQuote is not None:
        conn.write(
            """
            INSERT INTO company_quotes (company_symbol, price, change, change_percent)
            VALUES (%s, %s, %s, %s) 
            ON CONFLICT (company_symbol) DO UPDATE SET 
            (price, change, change_percent) = (EXCLUDED.price, EXCLUDED.change, EXCLUDED.change_percent)
            RETURNING company_symbol
            """,
            companyQuote.company_symbol.split(".")[0],
            companyQuote.price,
            companyQuote.change,
            companyQuote.change_percent,
        )

conn.close()

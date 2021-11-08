from db.conn import Conn
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import utils.companies as companies
from client.quote import get_companys_quote

conn = Conn(
    host="localhost",
    port=5432,
    database="riverfort_notification",
    user="riverfort",
    password="rgctechnology",
)

company_symbols = companies.get_company_symbols(conn=conn)
formatted_company_symbols = list(
    map(lambda company_symbol: f"{company_symbol}.L", company_symbols)
)
print(formatted_company_symbols)


conn.close()

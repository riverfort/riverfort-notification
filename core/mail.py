import os
import sys
import inspect
import traceback
from tabulate import tabulate

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from db.db.conn import Conn
from utils.company_quotes import get_top_gain_company_quotes
from mail.template_render import render_template
from mail.mail import send_email

conn = Conn(
    host="localhost",
    port=5432,
    database="riverfort_notification",
    user="riverfort",
    password="rgctechnology",
)

table = []
company_quotes = get_top_gain_company_quotes(conn=conn)
for company_quote in company_quotes:
    table.append(
        [
            company_quote.company_symbol,
            company_quote.company_name,
            company_quote.price,
            company_quote.change,
            company_quote.change_percent,
            company_quote.market_time,
        ]
    )

content = tabulate(
    table, headers=["Symbol", "Name", "Price", "Change", "Change %", "Time"]
)

try:
    with open("email.txt") as f:
        contacts = f.read().splitlines()
except:
    traceback.print_exc()
    sys.exit()

html = render_template("mail/templates/template.j2", **locals())
send_email(subject="Top Gainers: London", contacts=contacts, content=content, html=html)

conn.close()

import os
import sys
import inspect

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

company_quotes = get_top_gain_company_quotes(conn=conn)

contacts = ["tech@riverfortcapital.com", "qyang.nie@gmail.com"]
html = render_template("mail/templates/template.j2", **locals())
send_email(subject="Top Gainers: London", contacts=contacts, content="", html=html)

conn.close()

import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from mail.template_render import render_template
from mail.mail import send_email


item1 = "hello"
item2 = "world"

contacts = ["tech@riverfortcapital.com", "qyang.nie@gmail.com"]
html = render_template("mail/templates/template.j2", **locals())
send_email(subject="Top Gainers: London", contacts=contacts, content="Hello", html=html)

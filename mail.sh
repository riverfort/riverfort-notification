cd riverfort-notification
source venv/bin/activate
python db/write_company_quote.py
python core/mail.py
deactivate
cd

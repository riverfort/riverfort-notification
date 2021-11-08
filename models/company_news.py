class CompanyNews:
    def __init__(
        self, title, company_symbol, company_name, exchange, headline, pub_date, link
    ):
        super().__init__()
        self.title = title
        self.company_symbol = company_symbol
        self.company_name = company_name
        self.exchange = exchange
        self.headline = headline
        self.pub_date = pub_date
        self.link = link

    def __str__(self):
        return f"""CompanyNews: 
        - title: {self.title}
        - company_symbol: {self.company_symbol}
        - company_name: {self.company_name}
        - exchange: {self.exchange}
        - headline: {self.headline}
        - pub_date: {self.pub_date}
        - link: {self.link}
        """

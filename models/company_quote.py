class CompanyQuote:
    def __init__(self, company_symbol, company_name, price, change, change_percent):
        super().__init__()
        self.company_symbol = company_symbol
        self.company_name = company_name
        self.price = price
        self.change = change
        self.change_percent = change_percent

    def __str__(self):
        return f"""CompanyQuote: 
        - company_symbol: {self.company_symbol}
        - company_name: {self.company_name}
        - price: {self.price}
        - change: {self.change}
        - change_percent: {self.change_percent}
        """

class CompanyQuote:
    def __init__(self, company_symbol, price, change, change_percent):
        super().__init__()
        self.company_symbol = company_symbol
        self.price = price
        self.change = change
        self.change_percent = change_percent

    def __str__(self):
        return f"""CompanyQuote: 
        - company_symbol: {self.company_symbol}
        - price: {self.price}
        - change: {self.change}
        - change_percent: {self.change_percent}
        """

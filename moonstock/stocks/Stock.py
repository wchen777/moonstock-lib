class Stock:
    def __init__(self, name, price, change, change_percent, volume, market_cap, pe_ratio, eps, dividend_yield):
        self.name = name
        self.price = price
        self.change = change
        self.change_percent = change_percent
        self.volume = volume
        self.market_cap = market_cap
        self.pe_ratio = pe_ratio
        self.eps = eps
        self.dividend_yield = dividend_yield

    def __str__(self):
        return '{} {} {} {} {} {} {} {} {}'.format(
            self.name, self.price, self.change, self.change_percent, self.volume, self.market_cap, self.pe_ratio, self.eps, self.dividend_yield
        )

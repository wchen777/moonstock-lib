class Option:

    """
    A class to represent an option.

    ...

    Attributes
    ----------
    strike_price : float
        The strike price of the option.
    time_to_expiry : int
        The time to expiry of the option (in days).
    bid : float
        The bid price of the option.
    ask : float
        The ask price of the option.
    volume : int
        The volume of the option.
    option_type : str
        The type of the option (put or call, default is call).
    name : str
        The name of the option (optional).
    change : float
        The change in the option price.
    change_percent : float
        The change in the option price as a percentage.

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """

    def __init__(self, strike_price, time_to_expiry,
                 bid, ask, volume, option_type="call", name="option", change=None, change_percent=None):
        self.option_type = option_type
        self.strike_price = strike_price
        self.time_to_expiry = time_to_expiry
        self.bid = bid
        self.ask = ask
        self.name = name
        self.volume = volume
        self.change = change
        self.change_percent = change_percent

    # potentially do some tabling here
    def __str__(self) -> str:
        return "{} {} {} {} {} {} {} {} {}".format(
            self.name, self.strike_price, self.time_to_expiry, self.bid, self.ask, self.volume, self.change, self.change_percent, self.option_type
        )

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other) -> bool:
        return self.__dict__ == other.__dict__

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(self.__repr__())

import numpy as np
import math


class CAPM:
    """
    Class to represent a CAPM model

    Attributes
    ----------
    r_f : float
        Risk-free rate (fraction of 1)
    beta : float
        Beta of the CAPM model
    sigma : float
        Volatility of the CAPM model


    """

    def __init__(self, r_f, beta, sigma):
        """
        Constructor for the CAPM class

        Parameters
        ----------
        r_f : float
            Risk-free rate (fraction of 1)
        beta : float
            Beta of the CAPM model
        sigma : float
            Volatility of the CAPM model
        """
        self.r_f = r_f
        self.beta = beta
        self.sigma = sigma

    def get_expected_return_of_stock(self, stock_returns):
        """
        Calculates the expected return of a stock based on the CAPM model

        Parameters
        ----------
        stock_returns : numpy.array
            Array of stock returns

        :return: expected return of the stock
        """
        return self.r_f + self.beta * (stock_returns - self.r_f)

    def sml(self, stock_returns, market_returns):
        """
        Calculates the Sharpe ratio of a stock based on the CAPM model

        Parameters
        ----------
        stock_returns : numpy.array
            Array of stock returns
        market_returns : numpy.array
            Array of market returns

        :return: Sharpe ratio of the stock
        """
        return (self.get_expected_return_of_stock(stock_returns) - self.r_f) / self.sigma

import numpy as np
import math


def black_scholes(S, K, r, sigma, T, option_type='call'):
    """
    Calculate the theoretical price of a call or put option using the Black-Scholes formula

    :param S: stock price
    :param K: strike price
    :param r: risk-free rate
    :param sigma: volatility
    :param T: time to maturity
    option_type: 'call' or 'put'

    :return: price of the call or put option (in dollars)
    """

import numpy as np
from scipy.stats import norm
import math


def black_scholes(S, K, r, sigma, T, option_type='call'):
    """
    Calculate the theoretical price of a call or put option using the Black-Scholes model

    Parameters
    ----------

    S: stock price
    K: strike price
    r: risk-free rate
    sigma: volatility
    T: time to maturity (based on 1 annum as unit)
    option_type: 'call' or 'put'

    :return: price of the call or put option (in dollars)
    """

    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == 'call':
        return S * np.exp(-r * T) * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * np.exp(-r * T) * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")


def delta_black_scholes(S, K, r, sigma, T, option_type='call'):
    """
    Calculate the theoretical delta of a call or put option using the Black-Scholes model,
    or the total amount the option price is expected to move based on a $1 change in the underlying security.

    Parameters
    ----------

    S: stock price
    K: strike price
    r: risk-free rate
    sigma: volatility
    T: time to maturity (based on 1 annum as unit)
    option_type: 'call' or 'put'

    :return: delta of the call or put option (in dollars)
    """

    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))

    if option_type == 'call':
        return np.exp(-r * T) * norm.cdf(d1)
    elif option_type == 'put':
        return -np.exp(-r * T) * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")


def gamma_black_scholes(S, K, r, sigma, T, option_type='call'):
    """
    Calculate the theoretical gamma of a call or put option using the Black-Scholes model,
    or rate of change of the delta.

    Parameters
    ----------

    S: stock price
    K: strike price
    r: risk-free rate
    sigma: volatility
    T: time to maturity (based on 1 annum as unit)
    option_type: 'call' or 'put'

    :return: gamma of the call or put option (in dollars)
    """

    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))

    if option_type == 'call':
        return np.exp(-r * T) * norm.pdf(d1) / (S * sigma * math.sqrt(T))
    elif option_type == 'put':
        return -np.exp(-r * T) * norm.pdf(d1) / (S * sigma * math.sqrt(T))
    else:
        raise ValueError("option_type must be 'call' or 'put'")


def vega_black_scholes(S, K, r, sigma, T, option_type='call'):
    """
    Calculate the theoretical vega of a call or put option using the Black-Scholes model, or
    the amount the option price is expected to change based on a $1 change in the volatility.

    Parameters
    ----------

    S: stock price
    K: strike price
    r: risk-free rate
    sigma: volatility
    T: time to maturity (based on 1 annum as unit)
    option_type: 'call' or 'put'

    :return: vega of the call or put option (in dollars)
    """

    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))

    if option_type == 'call':
        return np.exp(-r * T) * S * norm.pdf(d1) * math.sqrt(T)
    elif option_type == 'put':
        return -np.exp(-r * T) * S * norm.pdf(d1) * math.sqrt(T)
    else:
        raise ValueError("option_type must be 'call' or 'put'")


def theta_black_scholes(S, K, r, sigma, T, option_type='call'):
    """
    Calculate the theoretical theta of a call or put option using the Black-Scholes model,
    or the the time decay of an option, the dollar amount an option will lose each day due to the passage of time.

    Parameters
    ----------

    S: stock price
    K: strike price
    r: risk-free rate
    sigma: volatility
    T: time to maturity (based on 1 annum as unit)
    option_type: 'call' or 'put'

    :return: theta of the call or put option (in dollars)
    """

    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))

    if option_type == 'call':
        return -(S * norm.pdf(d1) * sigma / (2 * math.sqrt(T))) - r * K * np.exp(-r * T) * norm.cdf(d1)
    elif option_type == 'put':
        return -(S * norm.pdf(d1) * sigma / (2 * math.sqrt(T))) + r * K * np.exp(-r * T) * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")


def rho_black_scholes(S, K, r, sigma, T, option_type='call'):
    """
    Calculate the theoretical rho of a call or put option using the Black-Scholes model,
    or the amount the option price changes relative to a unit change in the risk-free rate of interest.

    Parameters
    ----------

    S: stock price
    K: strike price
    r: risk-free rate
    sigma: volatility
    T: time to maturity (based on 1 annum as unit)
    option_type: 'call' or 'put'

    :return: rho of the call or put option (in dollars)
    """

    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))

    if option_type == 'call':
        return K * T * np.exp(-r * T) * norm.cdf(d1)
    elif option_type == 'put':
        return -K * T * np.exp(-r * T) * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")


# def implied_volatility_black_scholes(S, K, r, T, option_type='call', option_price=None, option_delta=None,
#                                      option_gamma=None, option_vega=None, option_theta=None, option_rho=None):
#     """
#     Calculate the implied volatility of a call or put option using the Black-Scholes model.

#     S: stock price
#     K: strike price
#     r: risk-free rate
#     T: time to maturity (based on 1 annum as unit)
#     option_type: 'call' or 'put'
#     option_price: option price (in dollars)
#     option_delta: option delta (in dollars)
#     option_gamma: option gamma (in dollars)
#     option_vega: option vega (in dollars)
#     option_theta: option theta (in dollars)
#     option_rho: option rho (in dollars)

#     :return: implied volatility of the call or put option (in dollars)
#     """

#     if option_price is None:
#         if option_delta is None or option_gamma is None or option_vega is None or option_theta is None or option_rho is None:
#             raise ValueError(
#                 "option_delta, option_gamma, option_vega, option_theta, option_rho must be provided")
#         else:
#             if option_type == 'call':
#                 option_price = option_delta + S * option_gamma + \
#                     0.5 * option_vega * S ** 2 + option_theta * S
#             elif option_type == 'put':
#                 option_price = option_delta - S * option_gamma - \
#                     0.5 * option_vega * S ** 2 + option_theta * S
#             else:
#                 raise ValueError("option_type must be 'call' or 'put'")

#         return newton_raphson(S, K, r, T, option_price, option_type)

import numpy as np
import math


def macaulay_duration(coupon_rate, maturity, frequency, coupon_payment_amount):
    """
    Calculates the Macaulay duration of a bond

    Parameters
    ----------
    coupon_rate : float
        Coupon rate of the bond (fraction of 1)
    maturity : float
        Maturity of the bond (in years)
    frequency : int
        Frequency of payments (in months)
    coupon_payment_amount : float
        Amount of the coupon payment (in dollars)

    """
    # Calculate the number of coupon payments
    num_coupons = math.ceil(maturity/frequency)
    # Calculate the total coupon amount
    total_coupon_amount = num_coupons * coupon_payment_amount
    # Calculate the total interest paid
    total_interest = total_coupon_amount * coupon_rate
    # Calculate the total principal paid
    total_principal = total_coupon_amount + total_interest
    # Calculate the Macaulay duration
    macaulay_duration = total_principal/total_interest
    return macaulay_duration


def macaulay_duration_from_yield(coupon_rate, maturity, frequency, coupon_payment_amount):
    """
    Calculates the Macaulay duration of a bond from a yield

    Parameters
    ----------
    coupon_rate : float
        Coupon rate of the bond (fraction of 1)
    maturity : float
        Maturity of the bond (in years)
    frequency : int
        Frequency of payments (in months)
    coupon_payment_amount : float
        Amount of the coupon payment (in dollars)

    """
    # Calculate the total interest paid
    total_interest = (coupon_rate * maturity * coupon_payment_amount) / \
        (1-math.pow(1+coupon_rate, -maturity/frequency))
    # Calculate the total principal paid
    total_principal = (coupon_payment_amount * maturity) / \
        (1-math.pow(1+coupon_rate, -maturity/frequency))
    # Calculate the Macaulay duration
    macaulay_duration = total_principal/total_interest
    return macaulay_duration

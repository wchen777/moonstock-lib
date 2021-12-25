import numpy as np
import math

# TODO: RETHINK THIS BOND CLASS


class Bond:
    """
    Class to represent a bond

    Attributes
    ----------

    coupon_rate : float
        Coupon rate of the bond (fraction of 1)

    maturity : float
        Maturity of the bond (in years)

    frequency : int
        Frequency of payments (in months)

    coupon_payment_amount : float
        Amount of the coupon payment (in dollars, substitute for coupon rate?)

    """

    def __init__(self, coupon_rate, maturity, frequency, coupon_payment_amount):
        """
        Constructor for the Bond class

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
        self.coupon_rate = coupon_rate
        self.maturity = maturity
        self.frequency = frequency
        self.coupon_payment_amount = coupon_payment_amount

    def macaulay_duration(self):
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
        num_coupons = math.ceil(self.maturity/self.frequency)
        # Calculate the total coupon amount
        total_coupon_amount = num_coupons * self.coupon_payment_amount
        # Calculate the total interest paid
        total_interest = total_coupon_amount * self.coupon_rate
        # Calculate the total principal paid
        total_principal = total_coupon_amount + total_interest
        # Calculate the Macaulay duration
        macaulay_duration = total_principal/total_interest
        return macaulay_duration

    # TODO: CHECK THIS FOR ACCURACY
    def yield_to_maturity(self):
        """
        Calculates the yield to maturity of a bond

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
        total_interest = (self.coupon_rate * self.maturity * self.coupon_payment_amount) / \
            (1-math.pow(1+self.coupon_rate, -self.maturity/self.frequency))
        # Calculate the total principal paid
        total_principal = (self.coupon_payment_amount * self.maturity) / \
            (1-math.pow(1+self.coupon_rate, -self.maturity/self.frequency))
        # Calculate the yield to maturity
        yield_to_maturity = total_interest/total_principal
        return yield_to_maturity

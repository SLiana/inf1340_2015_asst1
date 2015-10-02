#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2015. Stock transactions

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


#money = 1000.00
#print(money)

#Lakshmi's stock purchase
shares_bought = 2000.00
buy_price = 900.00
stock_buy_value = shares_bought * buy_price
buy_commission = 0.03 * (buy_price * shares_bought)
total_output = (buy_price) * (shares_bought) + (buy_commission)
print "Lakshmi bought", shares_bought, "stocks for", buy_price,"each, for a total of", stock_buy_value,"."
print "Lakshmi paid her stockbroker",buy_commission,"for the purchase."
print "After paying her stockbroker, Lakshmi's total payment was", total_output,"."

print"\n"

#Lakshmi's stock sale
shares_sold = 2000.00
sale_price = 942.75
stock_sale_value = shares_sold * sale_price
sale_commission = 0.03 * (sale_price * shares_sold)
total_intake = (sale_price) * (shares_sold) - (sale_commission)
print "Lakshmi sold" ,shares_sold, "shares for" ,sale_price, "each, for a total of" , stock_sale_value, "."
print "Lakshmi paid her stockbroker" ,sale_commission, "for the sale."
print "After paying her stockbroker, Lakshmi's total revenue from the sale was", total_intake,"."

print"\n"

#final calculation of Lakshmi's
print "After Lakshmi sold the stocks and paid the broker commission, she had", total_intake - total_output, "left."

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
stockbroker_buy_commission = 0.03 * (buy_price * shares_bought)
stock_buy_revenue = (buy_price) * (shares_bought) + (stockbroker_buy_commission)
print "Lakshmi bought", shares_bought, "stocks for", buy_price,"each, for a total of", stock_buy_value,"."
print "Lakshmi paid her stockbroker",stockbroker_buy_commission,"for the purchase."
print "After paying her stockbroker, Lakshmi's total payment was", stock_buy_revenue,"."

print"\n"

#Lakshmi's stock sale
shares_sold = 2000.00
sale_price = 942.75
stock_sale_value = shares_sold * sale_price
stockbroker_sale_commission = 0.03 * (sale_price * shares_sold)
stock_sale_revenue = (sale_price) * (shares_sold) - (stockbroker_sale_commission)
print "Lakshmi sold" ,shares_sold, "shares for" ,sale_price, "each, for a total of" , stock_sale_value, "."
print "Lakshmi paid her stockbroker" ,stockbroker_sale_commission, "for the sale."
print "After paying her stockbroker, Lakshmi's total revenue from the sale was", stock_sale_revenue,"."

print"\n"

#final calculation of Lakshmi's
print "After Lakshmi sold the stocks and paid the broker commission, she had", stock_buy_revenue - stock_sale_revenue, "left."

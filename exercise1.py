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





# Exercise 1: Stock Transactions (updated October 06, 2015)

# The cost of one share
buy_price = 900.00
 
# The number of shares Lakshmi  bought.
shares_bought = 2000.00

# Calculate stock buy value.
stock_buy_value = shares_bought * buy_price

# Calculate stockbrocker buy commision.
stockbroker_buy_commission = 0.03 * (buy_price * shares_bought)

# Calculate total output: the total amount Lakshmi spent on shares after she commissioned the stockbroker. 
total_output = stock_buy_value + stockbroker_buy_commission

print "Lakshmi bought", shares_bought, "stocks for", buy_price,"each, for a total of", stock_buy_value,"."
print "Lakshmi paid her stockbroker",stockbroker_buy_commission,"for the purchase."
print "After paying her stockbroker, Lakshmi's total payment was", total_output,"."

print"\n"

# The cost of one share
sale_price = 942.75
 
# The number of shares Lakshmi  sold.
shares_sold = 2000.00

# Calculate stock sale value.
stock_sale_value = shares_sold * sale_price

# Calculate stockbrocker sale commision.
stockbroker_sale_commission = 0.03 * (sale_price * shares_sold)

# Calculate total intake: the total amount Lakshmi received on shares after she commissioned the stockbroker. 
total_intake = stock_sale_value - stockbroker_sale_commission

print "Lakshmi sold", shares_sold, "stocks for", sale_price,"each, for a total of", stock_sale_value,"."
print "Lakshmi paid her stockbroker",stockbroker_sale_commission,"for the sale."
print "After paying her stockbroker, Lakshmi's total intake was", total_intake,"."

print"\n"

# Calculate whether Lakshmi made a profit or lost money.
final_amount = total_intake - total_output

if final_amount < 1:
    print "Lakshmi did not make a profit, since the amount of money after she sold the stock was", final_amount,"."
if final_amount > -1:
    print "Lakshmi made a profit, since the amount of money after she sold the stock was", final_amount,"."

print"\n"

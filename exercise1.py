#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2015. Stock transactions

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

input:
#Inputs: print "Lakshmi bought", shares_bought, "stocks for", buy_price,"each, for a total of", stock_buy_value,"."
#Expected Outputs: Lakshmi bought 2000.0 stocks for 900.0 each, for a total of1800000.0.
#Actual Output: Lakshmi bought 2000.0 stocks for 900.0 each, for a total of 1800000.0 .
#Errors: extra white space, solved with concantenation

#Inputs: print "After paying her stockbroker, Lakshmi's total payment was "+str(total_output)+"."
#print "Lakshmi sold "+str(shares_sold)+" stocks for "+str(sale_price)+" each, for a total of "+str(stock_sale_value)+"."
#Expected Outputs:
#After paying her stockbroker, Lakshmi's total payment was 1854000.0.
#
#
#Lakshmi sold 2000.0 stocks for 942.75 each, for a total of 1885500.0.
#Actual Output: After paying her stockbroker, Lakshmi's total payment was 1854000.0.
#Lakshmi sold 2000.0 stocks for 942.75 each, for a total of 1885500.0.
#Errors: no extra white space, solved by adding print"\n"

"""

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

print "Lakshmi bought "+str(shares_bought)+" stocks for "+str(buy_price)+" each, for a total of "+str(stock_buy_value)+"."
print "Lakshmi paid her stockbroker",stockbroker_buy_commission,"for the purchase."
print "After paying her stockbroker, Lakshmi's total payment was "+str(total_output)+"."

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

print "Lakshmi sold "+str(shares_sold)+" stocks for "+str(sale_price)+" each, for a total of "+str(stock_sale_value)+"."
print "Lakshmi paid her stockbroker",stockbroker_sale_commission,"for the sale."
print "After paying her stockbroker, Lakshmi's total intake was "+str(total_intake)+"."

print"\n"

# Calculate whether Lakshmi made a profit or lost money.
final_amount = total_intake - total_output

if final_amount <= 1:
    print "Lakshmi did not make a profit, since the amount of money she had after she sold the stock was "+str(final_amount)+"."
if final_amount >= -1:
    print "Lakshmi made a profit, since the amount of money she had after she sold the stock was "+str(final_amount)+"."

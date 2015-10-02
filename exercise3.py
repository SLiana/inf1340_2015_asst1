#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def diagnose_car():
    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs:

    Expected Outputs:

    Errors:

    """
    print "Please answer 'yes' or 'no' to the following questions so we can identify the possible issue with your car."
    silent = raw_input("Is the car silent when you turn the key?")
    if silent == 'yes' or 'YES' or 'Yes' or 'y' or 'Y':
        print "Are the battery terminals corroded?"
        corroded = raw_input()
        if corroded == 'yes' or 'YES' or 'Yes' or 'y' or 'Y':
            print "Clean terminals and try starting again."
        elif corroded == 'no':
            print "Replace cables and try again."
    elif silent == 'no':
        print "Does the car make a clicking noise?"
        clicking = raw_input()
        if clicking == 'yes' or 'YES' or 'Yes' or 'y' or 'Y':
            print "Replace the battery."
        if clicking == 'no':
            print "Does the car crank up but fails to start?"
            crank = raw_input()
            if crank == 'yes':
                print "Check spark plug connections."
            if crank == 'no':
                print "Does the engine start and then die?"
                start_and_die = raw_input()
                if start_and_die == 'no':
                    print "THERE'S NOTHING ON THE DECISION CHART FOR NO."
                if start_and_die == 'yes' or 'YES' or 'Yes' or 'y' or 'Y':
                    print "Does your car have fuel injection?"
                    fuel_injection = raw_input()
                    if fuel_injection == 'no':
                        print "Check to ensure the choke is opening and closing."
                    if fuel_injection == 'yes':
                        print "Get it in for service."
    else: #Prompt user to only enter yes or no
            print "Please enter only 'yes' or 'no'."
diagnose_car()

#




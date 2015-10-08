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
    print "Please enter either 'Y' or 'N' to the following questions so we can identify the possible issue with your car."
    silent = raw_input("Is the car silent when you turn the key? ")
    if silent == 'Y':
        print "Are the battery terminals corroded?"
        corroded = raw_input()
        if corroded == 'Y':
            print "Clean terminals and try starting again."
        elif corroded == 'N':
            print "Replace cables and try again."
    elif silent == 'N':
        print "Does the car make a clicking noise?"
        clicking = raw_input()
        if clicking == 'Y':
            print "Replace the battery."
        elif clicking == 'N':
            print "Does the car crank up but fails to start?"
            crank = raw_input()
            if crank == 'Y':
                print "Check spark plug connections."
            elif crank == 'N':
                print "Does the engine start and then die?"
                start_and_die = raw_input()
                if start_and_die == 'Y':
                    print "Does your car have fuel injection?"
                    fuel_injection = raw_input()
                    if fuel_injection == 'N':
                        print "Check to ensure the choke is opening and closing."
                    elif fuel_injection == 'Y':
                        print "Get it in for service."
                elif start_and_die == 'N':
                    print "Engine is not getting enough fuel. Clean fuel pump."
diagnose_car()






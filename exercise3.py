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
    silent = raw_input("Is the car silent when you turn the key? ")
    if silent == 'Y':
        corroded = raw_input("Are the battery terminals corroded?")
        if corroded == 'Y':
            print "Clean terminals and try starting again."
        elif corroded == 'N':
            print "Replace cables and try again."
    elif silent == 'N':
        clicking = raw_input("Does the car make a clicking noise?")
        if clicking == 'Y':
            print "Replace the battery."
        elif clicking == 'N':
            crank = raw_input("Does the car crank up but fails to start?")
            if crank == 'Y':
                print "Check spark plug connections."
            elif crank == 'N':
                start_and_die = raw_input("Does the engine start and then die?")
                if start_and_die == 'Y':
                    fuel_injection = raw_input("Does your car have fuel injection?")
                    if fuel_injection == 'N':
                        print "Check to ensure the choke is opening and closing."
                    elif fuel_injection == 'Y':
                        print "Get it in for service."
                elif start_and_die == 'N':
                    print "Engine is not getting enough fuel. Clean fuel pump."
diagnose_car()






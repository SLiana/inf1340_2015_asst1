#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs:

    Expected Outputs:

    Errors:

    """
    answer = raw_input("Please enter how many sides your shape has, and then hit 'Enter'")
    #The following answer is a cool party conversation starter. Try it sometime!
    if answer == '2':
        print "Fun fact - a polygon is a plane (2D) shape with straight sides. To be a regular polygon all the sides and angles must be the same."
    elif answer == '3':
        print "Triangle"
    elif answer == '4':
        print "Rectangle or square"
    elif answer == '5':
        print "Pentagon"
    elif answer == '6':
        print "Hexagon"
    elif answer == '7':
        print "Heptagon"
    elif answer == '8':
        print "Heptagon"
    elif answer == '9':
        print "Nonagon"
    elif answer == '10':
        print "Decagon"
    #More fun because sometimes writing code can be dry.
    elif answer == '42':
        print "I always thought something was fundamentally wrong with the universe."
    else:
        print "Error"

name_that_shape()
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


Update October 07, 2015

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
    
    Inputs: shape_name = raw_input("Please, enter how many sides your shape has and then hit 'Enter'")
    Expected Output: To have a space after 'Enter'.
    Actual Output: Please, enter how many sides your shape has and then hit 'Enter' (there was no space)
    Errors: There was no space after 'Enter'. We solved it by adding a space in the code after the single quatation following the word 'Enter' and before double quotation marks

    Inputs: shape_name = raw_input("Please, enter how many sides your shape has and then hit 'Enter' ")
            if shape_name == '2':
    Expected Output: To have a linebreak in the python function.
    Actual Output: There was no linebreak.
    Errors: missing print "\n". We solved it by adding print "\n"
    """

shape_name = raw_input("Please, enter how many sides your shape has and then hit 'Enter' ")
print "\n"

# Defining the shape names.
if shape_name == '2':
    print "Fun fact - a polygon is a plane (2D) shape with straight sides. To be a regular polygon all the sides and angles must be the same."
elif shape_name == '3':
    print "The shape you have chosen is 'Triangle'."
elif shape_name == '4':
    print "The shape you have chosen is 'Rectangle or square'."
elif shape_name == '5':
    print "The shape you have chosen is 'Pentagon'."
elif shape_name == '6':
    print "The shape you have chosen is 'Hexagon'."
elif shape_name == '7':
    print "The shape you have chosen is 'Heptagon'."
elif shape_name == '8':
    print "The shape you have chosen is 'Heptagon'."
elif shape_name == '9':
    print "The shape you have chosen is 'Nonagon'."
elif shape_name == '10':
    print "The shape you have chosen is 'Decagon'."
else:
    print "Error!"

name_that_shape()

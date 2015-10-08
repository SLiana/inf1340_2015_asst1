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
    else:
        print "Error"

name_that_shape()





 Assignment 1, Exercise 2 (October 06, 2015)
 
 
shape_name = raw_input("Please, enter how many sides your shape has and then hit 'Enter': ")
print "\n"

# Defining the shape names.
if shape_name == '2':
    print "Fun fact - a polygon is a plane (2D) shape with straight sides. To be a regular polygon all the sides and angles must be the same."
elif shape_name == '3':
    print "Thank you for using the Shape Name Finder. The shape you have chosen is 'Triangle'."
elif shape_name == '4':
    print "Thank you for using the Shape Name Finder. The shape you have chosen is 'Rectangle or square'."
elif shape_name == '5':
    print "Thank you for using the Shape Name Finder. The shape you have chosen is 'Pentagon'."
elif shape_name == '6':
    print "Thank you for using the Shape Name Finder. The shape you have chosen is 'Hexagon'."
elif shape_name == '7':
    print "Thank you for using the Shape Name Finder. The shape you have chosen is 'Heptagon'."
elif shape_name == '8':
    print "Thank you for using the Shape Name Finder. The shape you have chosen is 'Heptagon'."
elif shape_name == '9':
    print "Thank you for using the Shape Name Finder. The shape you have chosen is 'Nonagon'."
elif shape_name == '10':
    print "Thank you for using the Shape Name Finder. The shape you have chosen is 'Decagon'."

#More fun because sometimes writing code can be dry.
elif shape_name == '42':
    print "I always thought something was fundamentally wrong with the universe."
else:
    print "Error"

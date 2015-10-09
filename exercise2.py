#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"



    """
      """
    #For a given number of sides in a regular polygon, returns the shape name

   #Inputs: shape_name = raw_input("Please, enter how many sides your shape has and then hit 'Enter'")
   #Expected Output: To have a space after 'Enter'.
   #Actual Output: Please, enter how many sides your shape has and then hit 'Enter' (there was no space)
   #Errors: There was no space after 'Enter'. We solved it by adding a space in the code after the single quatation following the word 'Enter' and before double quotation marks

     """
    """
def name_that_shape():
    # Defining the shape names
    shape_name = raw_input("Please enter how many sides your shape has, and then hit 'Enter'. ")
    # Determine how many sides the shape has
    if shape_name == '3':
    # Tell the user the shap ename
        print "triangle"
    elif shape_name == '4':
        print "quadrilateral"
    elif shape_name == '5':
        print "pentagon"
    elif shape_name == '6':
        print "hexagon"
    elif shape_name == '7':
        print "heptagon"
    elif shape_name == '8':
        print "octagon"
    elif shape_name == '9':
        print "nonagon"
    elif shape_name == '10':
        print "decagon"
    else:
        print "Error"
name_that_shape()







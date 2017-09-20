# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:58:02 2017
Script for playing along in lectures
GEOG 5995_jendmurphy

@author: Jen Murphy
"""
#we can make functions in Python.  Python does not require us to specify the 
#type of input ie string etc.
def add(num1=0, num2=0):   #num1 and num2 default to zero
    return num1 + num2

print (add(3,2))

#we should try to avoid mutable defaults, eg a list is mutable so no good

#KWARG =  a keyword argument.  This allows us to name arguments

def add(num1,num2):
    return num1 + num2
answer = add(num2 = 3, num1 = 5)
print (answer)

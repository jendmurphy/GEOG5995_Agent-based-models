# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 08:55:32 2017

@author: gyjdm

AND NOW LETS MAKE SOME CHANGES!  Whoopity whoop.
"""
#shits and giggles


#First program in Python
message = "hello world"
bob = 1
jeff = bob*4
print (jeff)
print(message)

#setting up a function
def hi():
  print("hello world")
  print("hello you")

#running the function
hi()

#another way of doing this...
def hig(text):
  print(text)

hig("hello world again")

#now lets have a play with some numbers
def add2(num): #this is a function that applies the add2 to a number.
  return num + 2 #the function returns whatever num is, plus 2
  
answer = add2(5)#here we add a label to what is returned from the function, and give it 5 as the num
print(answer)#and then it prints the answer.

#Lets try a function that adds two undefined numbers together num and num2
def add(num,num2):
  return num+num2

#label the answer, and give the numbers
answer = add(5,7)
print(answer) #and print the answer!

#one way of checking code is to put in some print statements to check variables

#ANd another...
def add3(num, num2):
  a = num + num2
print(add(1,2))  
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:24:31 2017
AGENT BASED MODELLING PRACTICAL
@author:Jen Murphy

"""
# import random
import random
import operator
import matplotlib.pyplot

#Create a list for agents
agents = []

#AGENT 0
x0 = random.randint(0,100)
y0 = random.randint(0,100)

agents.append([x0,y0])
print(agents)

#AGENT 1
x1 = random.randint(0,100)
y1 = random.randint(0,100)

agents.append([x1,y1])
print(agents)

#Alternatively, we can do this without ever creating x or y.
agents.append([random.randint(0,100),random.randint(0,100)])
print(agents)

"""
max is a function which will look at the first item, and only look at the 
second if there is a tie - so it ignores the y coordinate in most
cases here
"""
print(max(agents))

"""
operator.itemgetter looks at item 1 in each pair in the list - remember that 
numbering starts at zero so this is the y coordinate.  Now we see the maximum
y coordinate
"""
print(max(agents, key=operator.itemgetter(1)))

"""
Then plot the agent locations using a library package which plots
"""
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.scatter(agents[0][0],agents[0][1], color = 'red')
matplotlib.pyplot.scatter(agents[1][0],agents[1][1], color = 'blue')
matplotlib.pyplot.scatter(agents[2][0],agents[2][1], color = 'green') 
matplotlib.pyplot.show()

"""
PRACTICAL 1 CODE NOT USED HERE

 # Make a x variable.
x0 = 50
x0#testing

 # Make a y variable.
y0 = 50
y0#testing

 # Change x and y based on random numbers.
#Generate random number
x0 = random.random()
x0#testing

y0 = random.random()
y0#testing
 # if random_number < 0.5:
 #     x0 = x0 + 1
 # else:
 #     x0 = x0 + 1
#FIRST ITERATION
if x0<0.5:
    x0 +=  1
if not x0<0.5:
    x0 -= 1
    
if y0<0.5:
    y0 +=  1
if not x0<0.5:
    y0 -= 1
    
# SECOND ITERATION
if x0<0.5:
    x0 +=  1
if not x0<0.5:
    x0 -= 1
    
if y0<0.5:
    y0 +=  1
if not x0<0.5:
    y0 -= 1

 # Make a second set of x and ys, and make these change randomly as well.

x1 = random.random()
y1=random.random()

#FIRST ITERATION X1 Y1
if x1<0.5:
    x1 += 1
else:
    x1 -= 1

if y1<0.5:  
    y1 += 1
else:
    y1 -= 1
#SECOND ITERATION X1 Y1
if x1<0.5:
    x1 += 1
else:
    x1 -= 1

if y1<0.5:  
    y1 += 1
else:
    y1 -= 1

 # Work out the distance between the two sets of x and ys.
distance = (((x1-x0)**2)+((y1-y0)**2))**0.5

#print locations and distance between agents
print(distance)
print(x0,y0)
print(x1,y1)

#testing
xi = 3
yi = 4
xj = 0
yj = 0
distance_ij = (((xi-xj)**2)+((yi-yj)**2))**0.5
print (distance_ij)
"""

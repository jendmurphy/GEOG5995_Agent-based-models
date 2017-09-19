# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:24:31 2017
CONTAINERS:  AGENT BASED MODELLING PRACTICAL
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
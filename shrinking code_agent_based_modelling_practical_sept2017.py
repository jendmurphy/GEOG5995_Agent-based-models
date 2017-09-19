# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:24:31 2017
SHRINKING CODE:  AGENT BASED MODELLING PRACTICAL
@author:Jen Murphy

"""
# import random
import random
import operator
import matplotlib.pyplot
#Add a variable to control the number of agents
num_of_agents = 10

#Create a list for agents
agents = []

#Use a for loop to create a number of agents within the list agents
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

print (agents)

# Now to optimise the random movement code
# To get x coordinates for agent i
for i in range(num_of_agents):
   if random.random() < 0.5:
       agents[i][0] += 1
       else :
           agents[i][0] -= 1
#  To get y coordinates for agent i
for i in range(num_of_agents):
    if random.random() < 0.5:
        agents[i][1] += 1
        else:
            agents[i][1] -= 1

#PLot the agents
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range (num_of_agents):
    matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
matplotlib.pyplot.show()





"""
Last practical's code

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
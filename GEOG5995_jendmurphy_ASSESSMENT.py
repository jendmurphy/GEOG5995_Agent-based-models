# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:24:31 2017
GEOG5995:  Introduction to Agent Based Models in Python
Core module for Data Analytics and Society integrated PhD

@author:Jen Murphy
"""
import matplotlib.pyplot
import operator
import agentframework
import csv
import random
import sys

#Define fixed variables
neighbourhood = 20
num_of_agents = 10
num_of_iterations = 100 

#Set up required lists
environment = [] # a list of rows of values - a 2D array defined by in.txt
agents = [] # a list of agentsm defined by agentframework.py

#Define function to randomise lists, code sourced from Stack Overflow
#Ref https://stackoverflow.com/a/9253366/8689056
def randomly(a):
    randomised = list(a)
    random.shuffle(randomised)
    return iter(randomised)

#Read in environment data
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

#Sort csv file into rows
for row in reader:				
    rowlist = [] 
    for value in row:				
        rowlist.append(value)
    environment.append(rowlist)
f.close() 

#plot environment
matplotlib.pyplot.imshow(environment)

#Make i agents, append coordinates to a list and plot the initial positions
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))

    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
    matplotlib.pyplot.imshow(environment)

#Move the agents j times, and plot the agent locations.
#The order in which agents are moved etc is random as per the randomly function defined above
for j in range (num_of_iterations):
    for i in randomly(range(num_of_agents)):
        agents[i].move()
        agents[i].eat()
        agents[i].share(neighbourhood)
#       agents[i].sick()       #Sick function within Agents class unused in final model

for i in range(num_of_agents):    
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
    matplotlib.pyplot.imshow(environment)
    
#  Agentframework has modified  ___str___ 
#  Print a list of all i agents, coordinates and stores
for i in range (num_of_agents):
    print(agents[i])

"""
# Loop through the agents in self.agents .
# Calculate the distance between self and the current other agent:     distance = self.distance_between(agent)               
# If distance is less than or equal to the neighbourhood         
# Sum self.store and agent.store         
# Divide sum by two to calculate average.         
# self.store = average             
# agent.store = average     
# End if 
# End loop 

# for agent in range (num_of_agents)
 #           self.agent = [agent[i]]

# Creat a function to randomise the lists, code found via Stack Overflow -credit Ned Batchelder 
def randomly(seq):
    shuffled = list(seq)
    random.shuffle(shuffled)
    return iter(shuffled)
    
    #OR alternative is to use a function called permutation from numpy...
#import numpy
#from numpy.random import permutation
#for i in permutation(1000):
    # do something with i
"""

"""For animating
#Define the variable fig - one snapshot of the agents
fig = matplotlib.pyplot.figure(figsize=(7,7))
#define the variable axes
ax = fig.add_axes([0,0,1,1])

#Make i agents, append coordinates to a list
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))

def update(frame_number):
    fig.clear()
    #Move the agents j times
    #for j in randomly(range (num_of_iterations)):
    for i in randomly(range(num_of_agents)):
        agents[i].move()
        agents[i].eat()
        agents[i].share(neighbourhood)
#           agents[i].sick()       
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
        matplotlib.pyplot.imshow(environment)
        
animation=matplotlib.animation.FuncAnimation(fig, update, interval=1)
fig.show()




#set up the numbners by running from command line.  argv[1] is num agents, next is num iterations.
#if len(sys.argv) < 1:
 #   num_of_agents = 10
#else: num_of_agents = int(sys.argv[1])

#if len(sys.argv) < 1:
 #   num_of_iterations = 100 
#else: num_of_iterations = int(sys.argv[2])













"""



"""
       
for i in range (num_of_agents):
    print(agents[1].store)

#Plot the position of agents
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
     matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show() 

# ___str___ has been modifid to show positions and stores
for i in range (num_of_agents):
    print(agents[i])
    


# This writes the environment as is now, to a new CSV file
f2 = open('dataout.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=' ')
for row in environment:
    writer.writerow(row)
f2.close()

"""


"""
# function distance_between returns the pythagorean distance between two given agents
def distance_between(agent0, agent1):
    return (((agent0.x-agent1.x)**2)+((agent0.y-agent1.y)**2))**0.5
distances = []

#Compare all agents with each other and compute distance.
#for j in range(num_of_agents):
 #   for i in range (num_of_agents):
  #          distance_between(agents[j],agents[i])    
   #         distances.append (distance_between(agents[j],agents[i]))
"""
"""
#Range will take up to 3 arguments, first one should be start of loop.
for j in range(num_of_agents):
    for i in range (j+1,num_of_agents):
            distance_between(agents[j],agents[i])    
            distances.append (distance_between(agents[j],agents[i]))
            print("Distance between agent {0} and {1} is {2}".format(j,i,distance_between(agents[j],agents[i])))
"""
#len(distances)
#print(distances)
#print(max(distances))
#print(min(distances))

#print(str(agents[0]))


"""
#trying to get some of the extra challenges done
import operator    # Do this line at the top of the code.
print(max(agents, key=operator.itemgetter(1)))    # Do this line at the bottom. 


"""
"""


#agent0 and agent1 take the input agents[i] where i is the position in the 
#list of the agent of interest


a = agentframework.Agent()
print (a.x, a.y)

a.move()
print (a.x, a.y)


#To time the running of the distance code
import datetime
def getTimeMS():
     dt = datetime.datetime.now()
     return dt.microsecond + (dt.second * 1000000) + \
     (dt.minute * 1000000 * 60) + (dt.hour * 1000000 * 60 * 60)

start = getTimeMS()






end = getTimeMS()
print("time = " + str(end - start))
"""
"""The code here compares all agents with all other agents and constructs a list of lists distances

for j in range(num_of_agents):
    row = []
    for i in range (num_of_agents):
        distance_between(agents[j],agents[i])    
        row.append (distance_between(agents[j],agents[i]))
    distances.append(row)

#set aside for now
"""

"""

#Define some functions and code for testing
agents.append([0,0])#set up two agents who we KNOW are 5 apart for testing
agents.append([3,4])#set up two agents who we KNOW are 5 apart for testing
print(agents)

# Work out the distance between agent 0 and agent 1
distance = (((agents[0][0]-agents[1][0])**2)+((agents[0][1]-agents[1][1])**2))**0.5


# import random
import random
import operator
import matplotlib.pyplot

#Add a variable to control the number of agents
num_of_agents = 10

#Create a list for agents_j
agents_j = []

#Use a for loop to create a number of agents within the list agents
for j in range(num_of_agents):
    agents_j.append([random.randint(0,100),random.randint(0,100)])

print (agents_j)

#Plot the agents with integer (0,100) range coordinates
matplotlib.pyplot.xlim(0, 100)
matplotlib.pyplot.ylim(0, 100)
for j in range (num_of_agents):
    matplotlib.pyplot.scatter(agents_j[j][0],agents_j[j][1])
matplotlib.pyplot.show()

# Now to optimise the random movement code and set up another set of agents.
# To get x coordinates for agent i
agents = []

for i in range(num_of_agents):
    agents [i][0] = random.random()
    agents [i][1] = random.random()

for i in range(num_of_agents):
    if agents[i][0] < 0.5:
       agents[i][0] += 1
    else :
       agents[i][0] -= 1

for i in range(num_of_agents):
    if agents[i][1] < 0.5:
       agents[i][1] += 1
    else :
       agents[i][1] -= 1

#PLot the agents
matplotlib.pyplot.xlim(-1, 2)
matplotlib.pyplot.ylim(-1, 2)
for i in range (num_of_agents):
    matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
matplotlib.pyplot.show()

"""
#INvestigating Boundary Issues
"""
# blur ---------------------------------------
import matplotlib.pyplot

data = []
processed_data = []

# Fill with random data.
for i in (range(0,99)):
    datarow = []
    for j in (range(0,99)):
        datarow.append(random.randint(0,255))
    data.append(datarow)

# Blur.
for i in (range(1,98)):
    datarow = []
    for j in (range(1,98)):
        sum = data[i][j]
        sum += data[i-1][j]
        sum += data[i+1][j]
        sum += data[i][j+1]
        sum += data[i][j-1]
        sum /= 5
    datarow.append(sum)
    processed_data.append(datarow)

matplotlib.pyplot.imshow(data)
matplotlib.pyplot.show()
matplotlib.pyplot.imshow(processed_data)
matplotlib.pyplot.show()



PRACTICAL 2 CODE NOW COMMENTED OUT


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
"""
max is a function which will look at the first item, and only look at the 
second if there is a tie - so it ignores the y coordinate in most
cases here
"""
"""
print(max(agents))
"""
"""
operator.itemgetter looks at item 1 in each pair in the list - remember that 
numbering starts at zero so this is the y coordinate.  Now we see the maximum
y coordinate
"""
"""
print(max(agents, key=operator.itemgetter(1)))
"""
"""
Then plot the agent locations using a library package which plots
"""
"""
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.scatter(agents[0][0],agents[0][1], color = 'red')
matplotlib.pyplot.scatter(agents[1][0],agents[1][1], color = 'blue')
matplotlib.pyplot.scatter(agents[2][0],agents[2][1], color = 'green') 
matplotlib.pyplot.show()
"""

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
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:24:31 2017
GEOG5995:  Introduction to Agent Based Models in Python
Core module for Data Analytics and Society Integrated PhD

@author:Jen Murphy

Code developed from practicals designed and delivered by Andy Evans, Leeds Institute for Data Analytics.
http://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/
"""
import matplotlib.pyplot
import operator
import agentframework
import csv
import random
import sys

#Define fixed variables
neighbourhood = 100
#num_of_agents = 10
#num_of_iterations = 100

#set up the numbers by running from command line.  argv[1] is num agents, next is num iterations.
#if len(sys.argv) < 1:
num_of_agents = 10
#else: num_of_agents = int(sys.argv[1])

#if len(sys.argv) < 1:
num_of_iterations = 100 
#else: num_of_iterations = int(sys.argv[2])

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


#For animating
#Define the variable fig - one snapshot of the agents
fig = matplotlib.pyplot.figure(figsize=(7,7))
#define the variable axes
ax = fig.add_axes([0,0,1,1])


#Make i agents, append coordinates to a list and plot the initial positions
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))
    


#  To set up animation
def update(frame_number):
    fig.clear()   

#  Move the agents j times, and plot the agent locations.
#  The order in which agents are moved etc is random as per the randomly function defined above

    for j in range (num_of_iterations):
        for i in randomly(range(num_of_agents)):
            agents[i].move()
            agents[i].eat()
            agents[i].share(neighbourhood)        
#           agents[i].sick()       #Sick function within Agents class unused in final model
    
#Plot the final position of agents within the environment
    for i in range(num_of_agents):    
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
        matplotlib.pyplot.imshow(environment)

#  Animate
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
fig.show()

#  To write the altered environment file to a new .csv
f2 = open('dataout.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=' ')
for row in environment:
    writer.writerow(row)
f2.close()

#  Agentframework has modified  ___str___ 
#  Prints a list of all i agents, coordinates and stores
for i in range (num_of_agents):
    print(agents[i])

"""
END OF CODE
"""
    

"""
SUPPLEMENTARY CODE RETAINED FOR LEARNING PURPOSES

#To time the code being run
import datetime
def getTimeMS():
     dt = datetime.datetime.now()
     return dt.microsecond + (dt.second * 1000000) + \
     (dt.minute * 1000000 * 60) + (dt.hour * 1000000 * 60 * 60)

start = getTimeMS() # starts timer

#code to be timed here
    
# Stop timer and print the time taken
end = getTimeMS()
print("time = " + str(end - start))



CALCULATING DISTANCES BETWEEN AGENTS - AND TESTING

#  Prior to developing agentframework, distances between agents calculated within main script
#  Function distance_between returns the pythagorean distance between two given agents

def distance_between(agent0, agent1):
    return (((agent0.x-agent1.x)**2)+((agent0.y-agent1.y)**2))**0.5
distances = []


#Compare all agents with each other and compute distance.
for j in range(num_of_agents):
    for i in range (num_of_agents):
            distance_between(agents[j],agents[i])    
            distances.append (distance_between(agents[j],agents[i]))

#  Inclusion of a (j+1) term allows removal of duplicated comparisons.
for j in range(num_of_agents):
    for i in range (j+1,num_of_agents):
            distance_between(agents[j],agents[i])    
            distances.append (distance_between(agents[j],agents[i]))
            print("Distance between agent {0} and {1} is {2}".format(j,i,distance_between(agents[j],agents[i])))

#  For i agents, there should be ((i^2 - i) /2) values within the list of distances if no self or multiple comparisons included

len(distances)  # tests the number of values given
print(max(distances))  #  maximum distance
print(min(distances))  #  minimum distance

#for testing purposes, simplified two agent list defined with a known distance
agents = []
agents.append([0,0])#set up two agents, known distance apart = 5
agents.append([3,4])#set up two agents, known distance apart = 5
print(agents)



PRACTICAL 2 CODE - SUPERCEDED

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



PRACTICAL 1 CODE - SUPERCEDED

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

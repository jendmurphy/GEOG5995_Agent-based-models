"""
Created on Wed Sep 20 14:55:33 2017
GEOG5995:  Introduction to Agent Based Models in Python
Core module for Data Analytics and Society integrated PhD

@author:Jen Murphy

Code developed from practicals designed and delivered by Andy Evans, Leeds Institute for Data Analytics.
http://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/
"""
import random

#  Define a class of agent within the environment
class Agent():
    def __init__(self,environment,agents):
        self.environment = environment
        self.agents = agents 
        self.store = 0  
        self.x = random.randint(0,300)
        self.y = random.randint(0,300)

#  Agents move within the environment.  Coordinates are updated based on a 
#  random number, moving +/- 1 for each iteration.
#  % is a torus boundary solution so that agents remain within the defined environment
#  TORUS boundary solution - allow agents leaving the top of an area to come in
#  at the bottom, and leaving left, come in on the right. 
    def move(self):
        if random.random() < 0.5:
             self.x = (self.x + 1) % 300
        else:
             self.x = (self.x - 1) % 300
             
        if random.random() < 0.5:
             self.y = (self.y + 1) % 300
        else:
             self.y = (self.y - 1) % 300

#  Agents reduce the number at their location in the environment by 10 every 
#  time they move.  NUmbers relate to the colour of the enviroment when plotted
#  so this can be seen as a gradual change in colour with more iterations.
    def eat(self): # make the agents really hungry 
         if self.environment[self.y][self.x] >= 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10       
         else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = self.environment[self.y][self.x]-self.environment[self.y][self.x]

#  When an agent has a store greater than 1000, the agent deposits all of their store in their current location
    def sick(self):
        if self.store >= 1000:            
            self.environment[self.y][self.x] +=1000
            self.store = self.store-1000

#  For this class, __str__ is defined such that we can easily print location and stores    
    def __str__(self):
        return (str(self.x) + "," + str(self.y) + "stores " + str(self.store))

#  Distance is defined as the pythagorean distance between two agents
    def distance(self,a):
             return (((self.x-a.x)**2)+((self.y-a.y)**2))**0.5  

#  Agents distribute stores equally amongst themselves when in proximity
#  Proximity is defined by neighboourhood
    def share(self, neighbourhood):
            for a in self.agents:
                if self.distance(a) <= neighbourhood:   
                    shared_store = (self.store + a.store)*0.5
                    self.store = a.store = shared_store
 

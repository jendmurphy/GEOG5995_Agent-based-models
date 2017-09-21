# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:55:33 2017

@author: Jen Murphy

CREATE A CLASS OF OBJECTS IN A FRAMEWORK
"""
import random

class Agent():
    def __init__(self,environment):
        self.environment = environment
        self.store = 0  
        self.x = random.randint(0,100)
        self.y = random.randint(0,100)     
 
    def move(self):
        if random.random() < 0.5:
             self.x = (self.x + 1) % 99
        else:
             self.x = (self.x - 1) % 99
             
        if random.random() < 0.5:
             self.y = (self.y + 1) % 99
        else:
             self.y = (self.y - 1) % 99

    def eat(self): # can you make it eat what is left?
         if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10 

    def __str__(self):
        return (str(self.x) + " " + str(self.y))



""" 
# Make the agents.
 for i in range(num_of_agents):
     agents.append([random.randint(0,100),random.randint(0,100)])

 # Move the agents.
 for j in range(num_of_iterations):
     for i in range(num_of_agents):

         if random.random() < 0.5:
             agents[i][0] = (agents[i][0] + 1) % 99
         else:
             agents[i][0] = (agents[i][0] - 1) % 99

         if random.random() < 0.5:
             agents[i][1] = (agents[i][1] + 1) % 99
         else:
             agents[i][1] = (agents[i][1] - 1) % 99

def randomise(self):
        self.x = (random.randint(0,100))
        self.y = (random.randint(0,100)) 
        

             
"""
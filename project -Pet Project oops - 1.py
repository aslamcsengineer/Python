# -*- coding: utf-8 -*-
"""
Pet class with name ,hunger at 0 and energy 
for play hunger will get+=5 energy-=5 
"""

class Pet:
    def __init__(self,name):
        self.name = name
        self.energy = 100
        self.hunger = 0 
    def name_function(self):
        print(f"Pet name {self.name}")
    def play(self):
        self.hunger+=5
        self.energy-=5
        print(f"{self.name} Energy = {self.energy}\n{self.name} Hunger = {self.hunger}")
    def sleep(self):
        self.energy+=5
        print(f"{self.name} Energy Restored = ",self.energy)
    def feed(self):
        self.hunger-=5
        print(f"{self.name} Hunger Decreased = ",self.hunger)
a = Pet("Cat")
b = Pet("Dog")

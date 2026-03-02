# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 21:52:28 2026

@author: moham
"""

class Character:
    # BUG 2 FIXED: Removed 'health' from the parentheses
    def __init__(self, name):
        self.__health = 100
        self.name = name
        
    def take_damage(self, damage_amount):
        self.__health -= damage_amount
        # Replaced the 'X' with the actual health!
        print(f"Ouch! {self.name}'s Health is now {self.__health}")

    # BUG 4 FIXED: We add a safe way to 'get' the hidden health
    def get_health(self):
        return self.__health

class Warrior(Character):
    # Notice we ask for 'starting_rage' here
    def __init__(self, name, starting_rage):
        # BUG 1 FIXED: Added () to super()
        super().__init__(name) 
        
        # We assign the starting_rage we passed in!
        self.rage = starting_rage 
        
    # BUG 3 FIXED: Added __ to the end, and used 'return'
    def __str__(self):
        # BUG 4 FIXED: We use self.get_health() instead of self.__health
        return f"{self.name} the Warrior \nHealth: {self.get_health()} | Rage: {self.rage}"

# --- Test Area ---

# We create the Warrior with the name "Aslam" and 33 starting rage
a = Warrior("Aslam", 33) 

# Because we wrote a beautiful __str__ method, we can just print the object!
print(a)

print("\n--- Battle ---")
a.take_damage(20)
from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight 
        
    @abstractmethod
    def use(self):
        pass

class Potion(Item):
    # PRO-TIP: We don't even need __init__ here! 
    # Python automatically uses the Item parent's __init__ to set name/weight.
    
    def use(self):
        print(f"You drank the {self.name}. Health Restored!")

class Sword(Item):
    # Same here! It automatically inherits the parent's setup.
    
    def use(self):
        print(f"You swung the {self.name} for 10 damage!")

class Player:
    def __init__(self, name):
        self.name = name 
        self.inventory = []
        
    # Changed 'name' to 'item' so it's clearer what we are adding
    def add_item(self, item):
        self.inventory.append(item)
        
    def use_all(self):
        for item in self.inventory:
            # THE FIX: We call the abstract method!
            item.use() 
            
# --- TEST AREA (Sample I/O) ---

hero = Player("Arthur")
print(f"Hero created: {hero.name}")

health_pot = Potion("Minor Health Potion", 1.5)
iron_sword = Sword("Rusty Iron Sword", 5.0)

hero.add_item(health_pot)
hero.add_item(iron_sword)

print(f"{hero.name} has {len(hero.inventory)} items in their bag.")

print("\n--- Action Phase ---")
hero.use_all()
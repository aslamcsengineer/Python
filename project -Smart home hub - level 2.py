class SmartDevice:
    def __init__(self,name):
        self.name = name
        self.__is_on = False
    def toggle_power(self):
        if self.__is_on:
            print("Turned Of ",self.name)
            self.__is_on = False 
        else:
            print("Turned On",self.name)
            self.__is_on = True 
    def get_status(self):
        return self.__is_on
class SmartLight(SmartDevice):
    def __init__(self,name,brightness):
        self.brightness = brightness
        super().__init__(name)
    def __str__(self):
        if(self.get_status() == True):
            return(f"Light : {self.name}\nPower : On\n brightness = {self.brightness}")
        else:
            return(f"Light : {self.name}\nPower : Off")
class SmartThermostat(SmartDevice):
    def __init__(self,name,temperature):
        super().__init__(name)
        self.temperature = temperature
    def __str__(self):
        if(self.get_status() == True):
            return (f"AC : {self.name}\nPower : On\ntemperature = {self.temperature}")
        else:
            return (f"AC : {self.name}\nPower : Off")
my_light = SmartLight("Living room lamp", 80)
my_ac = SmartThermostat("Bedroom Ac", 20)
print(my_light)
print(my_ac)
my_light.toggle_power()
my_ac.toggle_power()
print(my_light)
print(my_ac)
my_light.toggle_power()
my_ac.toggle_power()
print(my_light)
print(my_ac)



        
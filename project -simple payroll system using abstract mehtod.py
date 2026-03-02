# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 06:45:43 2026

@author: moham
"""
#The payroll system
from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def calculate_pay(self):
        pass
    
class SalariedEmplyee(Employee):
    def __init__(self, name,monthly_salary):
        self.monthly_salary = monthly_salary
        super().__init__(name)
    def calculate_pay(self):
        return self.monthly_salary
    
class HourlyEmployee(Employee):
    def __init__(self,name,hourly_wage,hourly_worked):
        self.hourly_wage  = hourly_wage
        self.hourly_worked = hourly_worked
        super().__init__(name)

    def calculate_pay(self):
        return self.hourly_wage*self.hourly_worked

alice = SalariedEmplyee("Alice", 50000)
bob = HourlyEmployee("Bob", 30, 20)
my_employees = [alice,bob]
for worker in my_employees:
    print(f"{worker.name} gets paid ${worker.calculate_pay()}")
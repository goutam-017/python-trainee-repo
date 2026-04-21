class Bike:
    name='Mauntain Bike'
    gear=6

bike1=Bike()
print(f'Name: {bike1.name}, It have {bike1.gear} gear')


class Employee:
    employee_id = 0

employee1 = Employee()
employee2 = Employee()

employee1.employeeID = 1001
print(f"Employee ID: {employee1.employeeID}")

employee2.employeeID = 1002
print(f"Employee ID: {employee2.employeeID}")

class Room:
    length=0.0
    breadth=0.0

    def calculate_area(self):
        total=self.length*self.breadth
        print(f'Area of room is= {total}')

room=Room()
room.length=float(input("Enter Length= "))
room.breadth=float(input("Enter breadth= "))
room.calculate_area()

class NewBike:
    def __init__(self,name):
        self.name=name
    def dis(self):
        print(self.name)

new_bike=NewBike('Mountain Bike')
new_bike.dis()

# inheritance
class Animal:
    name=''
    def eat(self):
        print("I can eat.")

class Dog(Animal):
    def display(self):
        print(f'My name is {self.name}.')

dog=Dog()
dog.name='Sheru'
dog.display()
dog.eat()
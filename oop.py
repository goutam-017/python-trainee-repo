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

class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name+ ' ' + str(abc.age))

p1 = Person("Emil", 36)
p1.greet()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()


class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
  x.move()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def get_age(self):
        return self.__age


p1 = Person("Emil", 25)
print(p1.name)
print(p1.get_age())


# encapsulation
class Student:
    def __init__(self,name):
        self.name=name
        self.__marks=0

    def set_grade(self,marks):
        if(0<=marks<=100):
            self.__marks=marks
        else:
            return 'Grade must be between 0 and 100'

    def get_grade(self):
        return f'Your grade is {self.__marks}'

    def get_status(self):
        if(self.__marks>=40):
            return 'You are passed'
        else:
            return 'You are failed'
        
s1=Student('Goutam')
s1.set_grade(30)
print(s1.get_grade())
print(s1.get_status())

class Demo:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def get_data(self):
        return self.__age

p1=Demo('Goutam',22)
print(p1._Demo__age)
print(p1.get_data())


# inner class 
class Outer:
    def __init__(self,name):
        self.name=name

    class Inner:
        def __init__(self,outer):
            self.outer=outer

        def display(self):
            print(f'Outer class name {self.outer.name}')

outer=Outer('goutam')
inner=outer.Inner(outer)
inner.display()
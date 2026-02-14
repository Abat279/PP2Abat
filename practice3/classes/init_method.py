#  1
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Ali")
print(p1.name)


#  2
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

car1 = Car("Toyota", 2023)
print(car1.brand, car1.year)


#  3
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

r = Rectangle(5, 10)
print(r.width * r.height)


#  4
class Student:
    def __init__(self, name, grade=12):
        self.name = name
        self.grade = grade

s1 = Student("Erkebulan")
print(s1.name, s1.grade)


#  5
class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

l1 = Laptop("HP", 16)
print(l1.brand, l1.ram)
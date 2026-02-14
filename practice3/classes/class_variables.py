#  1
class Student:
    university = "KBTU"

s1 = Student()
s2 = Student()
print(s1.university, s2.university)


#  2
class Car:
    wheels = 4

car1 = Car()
print(car1.wheels)


#  3
class Person:
    country = "Kazakhstan"

p1 = Person()
p2 = Person()
p2.country = "USA"

print(p1.country)
print(p2.country)


#  4
class Animal:
    kingdom = "Mammal"

a1 = Animal()
Animal.kingdom = "Animal"
print(a1.kingdom)


#  5
class Laptop:
    brand = "HP"

l1 = Laptop()
l2 = Laptop()
Laptop.brand = "Dell"
print(l1.brand, l2.brand)
#  1
class Person:
    pass

p1 = Person()
print(type(p1))


#  2
class Car:
    brand = "Toyota"

car1 = Car()
print(car1.brand)


#  3
class Animal:
    species = "Dog"

animal1 = Animal()
animal2 = Animal()
print(animal1.species, animal2.species)


#  4
class Book:
    title = "Python Basics"

book1 = Book()
print(book1.title)


#  5
class Student:
    university = "KBTU"

s1 = Student()
print(s1.university)

# 1
class Animal:
    def speak(self):
        print("Animal sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

c = Cat()
c.speak()


# 2
class Vehicle:
    def move(self):
        print("Vehicle moves")

class Bike(Vehicle):
    def move(self):
        print("Bike moves")

b = Bike()
b.move()


# 3
class Person:
    def introduce(self):
        print("I am a person")

class Teacher(Person):
    def introduce(self):
        print("I am a teacher")

t = Teacher()
t.introduce()


# 4
class Shape:
    def area(self):
        print("Calculating area")

class Square(Shape):
    def area(self):
        print("Area = side * side")

s = Square()
s.area()


# 5
class Bird:
    def sound(self):
        print("Bird sound")

class Parrot(Bird):
    def sound(self):
        print("Parrot talks")

p = Parrot()
p.sound()
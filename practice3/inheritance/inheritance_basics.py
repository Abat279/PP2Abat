# 1
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    pass

d1 = Dog()
d1.speak()


# 2
class Vehicle:
    def move(self):
        print("Moving")

class Car(Vehicle):
    pass

c1 = Car()
c1.move()


# 3
class Person:
    def greet(self):
        print("Hello")

class Student(Person):
    pass

s1 = Student()
s1.greet()


# 4
class Shape:
    def info(self):
        print("This is a shape")

class Circle(Shape):
    pass

circle = Circle()
circle.info()


# 5
class Bird:
    def fly(self):
        print("Flying")

class Eagle(Bird):
    pass

e = Eagle()
e.fly()
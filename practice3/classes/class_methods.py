#  1
class Person:
    def greet(self):
        print("Hello!")

p1 = Person()
p1.greet()


#  2
class Dog:
    def bark(self):
        print("Woof!")

d1 = Dog()
d1.bark()


#  3
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(3, 4))


#  4
class Student:
    def introduce(self):
        print("I am a student")

s1 = Student()
s1.introduce()


#  5
class Circle:
    def area(self, radius):
        return 3.14 * radius ** 2

c1 = Circle()
print(c1.area(5))
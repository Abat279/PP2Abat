# 1
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s1 = Student("Ali", 12)
print(s1.name, s1.grade)


# 2
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof")

d = Dog()
d.speak()


# 3
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand)
        self.year = year

c = Car("Toyota", 2023)
print(c.brand, c.year)


# 4
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        super().show()
        print("Class B")

b = B()
b.show()


# 5
class Shape:
    def describe(self):
        print("General shape")

class Rectangle(Shape):
    def describe(self):
        super().describe()
        print("Rectangle shape")

r = Rectangle()
r.describe()
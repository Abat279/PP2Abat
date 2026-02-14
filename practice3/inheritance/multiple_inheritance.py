# 1
class Father:
    def skills(self):
        print("Driving")

class Mother:
    def talents(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skills()
c.talents()


# 2
class A:
    def method_a(self):
        print("Method A")

class B:
    def method_b(self):
        print("Method B")

class C(A, B):
    pass

obj = C()
obj.method_a()
obj.method_b()


# 3
class Writer:
    def write(self):
        print("Writing")

class Speaker:
    def speak(self):
        print("Speaking")

class Person(Writer, Speaker):
    pass

p = Person()
p.write()
p.speak()


# 4
class Engine:
    def start(self):
        print("Engine started")

class Wheels:
    def rotate(self):
        print("Wheels rotating")

class Car(Engine, Wheels):
    pass

car = Car()
car.start()
car.rotate()


# 5
class X:
    def show_x(self):
        print("X")

class Y:
    def show_y(self):
        print("Y")

class Z(X, Y):
    def show_all(self):
        self.show_x()
        self.show_y()

z = Z()
z.show_all()
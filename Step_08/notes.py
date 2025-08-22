# ====================================================
#           Object Oriented Programming (OOP) in Python
# ====================================================

# OOP is a way of writing code using "classes" and "objects".
# It helps make code reusable, secure, and modular.

"""
4 Pillars of OOP:
1. Abstraction
2. Encapsulation
3. Inheritance
4. Polymorphism
"""

# ====================================================
# 1. Abstraction
# ====================================================
# Hiding unnecessary details and showing only the important part.
# Example: When driving a car, we only know "start" or "stop".
# We don’t care how the engine works internally.


class Car:
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")


car1 = Car()
car1.start()
car1.stop()


# ====================================================
# 2. Encapsulation
# ====================================================
# Wrapping "data" (variables) and "methods" (functions) inside a class.


class Account:
    def __init__(self, balance, account):
        self.balance = balance
        self.account_no = account

    def debit(self, amount):
        self.balance -= amount
        print("RS", amount, "debited from", self.account_no)
        print("Total Balance =", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("RS", amount, "credited to", self.account_no)
        print("Total Balance =", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, "Ausaf Ul Islam")
acc1.debit(1000)
acc1.credit(500)


# ---------------- Private Attributes ----------------
class SafeAccount:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  # private (not directly accessible)

    def show_pass(self):  # allowed inside class
        return self.__acc_pass


acc2 = SafeAccount("12345", "mypassword")
print(acc2.acc_no)
print(acc2.show_pass())  # correct way


# ====================================================
# 3. Inheritance
# ====================================================
# One class (child) can use code from another class (parent).


class Car:
    def start(self):
        print("Car started..")

    def stop(self):
        print("Car stopped..")


class ToyotaCar(Car):  # ToyotaCar inherits Car
    def __init__(self, name):
        self.name = name


car1 = ToyotaCar("Fortuner")
car1.start()  # using parent method


# ------------ Multilevel Inheritance ------------
class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type


car2 = Fortuner("Diesel")
car2.start()


# ------------ Multiple Inheritance ------------
class A:
    varA = "Class A"


class B:
    varB = "Class B"


class C(A, B):  # inherits from both A and B
    varC = "Class C"


c1 = C()
print(c1.varA, c1.varB, c1.varC)


# ====================================================
# Super() Keyword
# ====================================================
class Car:
    def __init__(self, type):
        self.type = type


class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)  # call parent constructor


car3 = ToyotaCar("Prius", "Electric")
print(car3.type)


# ====================================================
# Class Method
# ====================================================
class Person:
    name = "Ausaf"

    @classmethod
    def changeName(cls, new_name):
        cls.name = new_name  # affects class variable


print(Person.name)
Person.changeName("Afaq")
print(Person.name)


# ====================================================
# Property Method
# ====================================================
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def fullname(self):  # now works like a variable
        return f"{self.fname} {self.lname}"


p1 = Person("Ausaf", "Islam")
print(p1.fullname)  # no () needed


# ====================================================
# 4. Polymorphism
# ====================================================
# One name, many forms.

print(len("Ausaf"))  # string
print(len([1, 2, 3]))  # list


class Animal:
    def sound(self):
        print("Some animal sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


class Cat(Animal):
    def sound(self):
        print("Meow")


a1 = Dog()
a2 = Cat()
a1.sound()
a2.sound()

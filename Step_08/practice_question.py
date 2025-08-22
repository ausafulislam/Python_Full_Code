# ====================================================
#                 Python Practice Questions
# ====================================================

# NOTE:
# These are beginner-friendly Python practice questions.
# Try solving each one on your own before checking the solutions.
# Topic: Object Oriented Programming (OOP)

# --------------------------------------------------------------------------
# 01: Create a Student class that takes name & marks of 3 subjects
#     as arguments in constructor. Then create a method to print the average.
# --------------------------------------------------------------------------


class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average(self):
        return (self.marks1 + self.marks2 + self.marks3) / 3


s1 = Student("Ausaf", 90, 80, 70)
print("Average Marks:", s1.average())


# --------------------------------------------------------------------------
# 02: Create an Account class with 2 attributes - balance & account_number.
#     Create methods for debit, credit, and printing the balance.
# --------------------------------------------------------------------------


class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "Credited")

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "Debited")

    def print_balance(self):
        print("Account:", self.account_number, "| Balance:", self.balance)


acc1 = Account("12345", 1000)
acc1.print_balance()

acc1.credit(500)
acc1.print_balance()

acc1.debit(200)
acc1.print_balance()


# --------------------------------------------------------------------------
# 03: Define a Circle class with radius as constructor argument.
#     Add area() and perimeter() methods.
# --------------------------------------------------------------------------


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2 * 3.14 * self.radius


c1 = Circle(21)
print("Area of Circle:", c1.area())
print("Perimeter of Circle:", c1.perimeter())


# --------------------------------------------------------------------------
# 04: Define an Employee class with role, department and salary.
#     Create an Engineer class that inherits from Employee
#     and adds name and age.
# --------------------------------------------------------------------------


class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def show_details(self):
        print("Role:", self.role)
        print("Department:", self.department)
        print("Salary:", self.salary)


class Engineer(Employee):
    def __init__(self, name, age, role, department, salary):
        super().__init__(role, department, salary)
        self.name = name
        self.age = age

    def show_details(self):
        super().show_details()
        print("Name:", self.name)
        print("Age:", self.age)


e1 = Engineer("Alice", 30, "Manager", "Sales", 50000)
e1.show_details()


# --------------------------------------------------------------------------
# 05: Create an Order class which stores items and prices.
#     Use the __gt__() method to compare orders by price.
# --------------------------------------------------------------------------


class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, other):  # "greater than" operator overload
        return self.price > other.price


order1 = Order("Item1", 100)
order2 = Order("Item2", 200)

print(order1 > order2)  # False
print(order2 > order1)  # True

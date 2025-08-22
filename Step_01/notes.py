# ==================================================== #
#                Variables in Python
# ==================================================== #

# A variable is a name (identifier) that stores a value.
# It's like a label attached to a piece of data stored in memory.

# Example:
my_name = "ausafulislam"  # string value
my_age = 23  # integer value
is_married = False  # boolean value

# Breakdown:
# my_name        → variable name (identifier)
# =              → assignment operator
# "ausafulislam" → value assigned to the variable


# ==================================================== #
#                Data Types in Python
# ==================================================== #

# Data types define the type of value a variable can hold.

# Common Python data types:

# 1. String (str) – a sequence of characters enclosed in quotes
var_1 = "Ausaf is a great person"
print(type(var_1))  # <class 'str'>

# 2. Integer (int) – whole numbers without decimals
var_2 = 123
print(type(var_2))  # <class 'int'>

# 3. Float (float) – numbers with decimals
var_3 = 12.3
print(type(var_3))  # <class 'float'>

# 4. Boolean (bool) – True or False
var_4 = True
print(type(var_4))  # <class 'bool'>

# 5. NoneType – represents the absence of a value
var_5 = None
print(type(var_5))  # <class 'NoneType'>


# ==================================================== #
#                Operators in Python
# ==================================================== #

# Operators are special symbols used to perform operations on variables and values.

# ---------------------------- #
# 1. Arithmetic Operators      #
# (+, -, *, /, %, **, //)      #
# ---------------------------- #
n_1 = 2
n_2 = 2

print(n_1 + n_2)  # 4   (Addition)
print(n_1 - n_2)  # 0   (Subtraction)
print(n_1 * n_2)  # 4   (Multiplication)
print(n_1 / n_2)  # 1.0 (Division - float result)
print(n_1 % n_2)  # 0   (Modulus - remainder)
print(n_1**n_2)  # 4   (Exponentiation)
print(n_1 // n_2)  # 1   (Floor Division)


# ---------------------------------------- #
# 2. Comparison (Relational) Operators     #
# (==, !=, >, <, >=, <=)                   #
# ---------------------------------------- #
print(n_1 == n_2)  # True
print(n_1 != n_2)  # False
print(n_1 > n_2)  # False
print(n_1 < n_2)  # False
print(n_1 >= n_2)  # True
print(n_1 <= n_2)  # True


# ----------------------------------- #
# 3. Assignment Operators             #
# (=, +=, -=, *=, /=, %=, **=, //=)   #
# ----------------------------------- #
n_3 = 5
print(n_3)  # 5

n_3 = n_3 + 5
print(n_3)  # 10

n_3 += 5
print(n_3)  # 15

n_3 -= 5
print(n_3)  # 10

n_3 *= 5
print(n_3)  # 50

n_3 /= 5
print(n_3)  # 10.0

n_3 %= 5
print(n_3)  # 0.0

n_3 = 10
n_3 **= 5
print(n_3)  # 100000

n_3 //= 5
print(n_3)  # 20000


# ---------------------------- #
# 4. Logical Operators         #
# (and, or, not)               #
# ---------------------------- #
print(True and True)  # True
print(True and False)  # False

print(True or False)  # True
print(False or False)  # False

print(not True)  # False
print(not False)  # True

# Note: Logical operators can also be used with non-boolean values.


# ==================================================== #
#                Type Conversion in Python
# ==================================================== #

# Type Conversion = changing one data type to another
# Types:
# 1. Implicit Conversion – automatic by Python
# 2. Explicit Conversion – manual using int(), float(), str(), etc.

# -------- Implicit Conversion --------
x = 10  # int
y = 3.5  # float
z = x + y  # int + float → float
print(z)  # 13.5
print(type(z))  # <class 'float'>

# -------- Explicit Conversion --------
num_str = "123"
num_int = int(num_str)  # string → int
print(num_int)  # 123

f = 5.9
i = int(f)  # float → int (decimal removed)
print(i)  # 5

age = 25
age_str = str(age)  # int → string
print(age_str)  # "25"


# ==================================================== #
#                     Input in Python
# ==================================================== #

# input() function is used to take input from the user.
# By default, input is taken as a string.

# -------- Basic Input --------
name = input("Enter your name: ")
print("Hello,", name)

# -------- Input with Type Conversion --------
age = int(input("Enter your age: "))
print("Your age + 5 will be:", age + 5)

height = float(input("Enter your height in meters: "))
print("Your height is:", height, "meters")

# -------- Boolean-like Input --------
married_input = input("Are you married? (yes/no): ")
is_married = married_input == "yes"
print("Married status:", is_married)

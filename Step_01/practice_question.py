# ==================================================== #
#                 Python Practice Questions            #
# ==================================================== #

# NOTE:
# These are beginner-friendly Python practice questions.
# Try solving each one on your own before looking at the answers.
# Topics covered: input/output, variables, data types,
# arithmetic operations, and conditionals.

# ---------------------------------------------------- #
# 1. Write a program to input 2 numbers and print their sum.
# ---------------------------------------------------- #

# Solution
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
print("Sum:", num_1 + num_2)

# ---------------------------------------------------- #
# 2. Write a program to input the side of a square and print its area.
# ---------------------------------------------------- #

# Solution
side = int(input("Enter the side of the square: "))
print("Area of square:", side**2)

# ---------------------------------------------------- #
# 3. Write a program to input 2 floating-point numbers and print their average.
# ---------------------------------------------------- #

# Solution
num_1 = float(input("Enter first floating-point number: "))
num_2 = float(input("Enter second floating-point number: "))
print("Average:", (num_1 + num_2) / 2)

# ---------------------------------------------------- #
# 4. Write a program to input 2 integers, a and b.
#    Print True if a is greater than or equal to b,
#    otherwise print False.
# ---------------------------------------------------- #

# Solution
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
print(a >= b)

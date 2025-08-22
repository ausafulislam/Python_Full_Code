# ==================================================== #
#               Functions and Recursion                #
# ==================================================== #

# -------------------------------
# Functions in Python
# -------------------------------

# There are 2 types of functions in Python:
# 1. Built-in Functions – provided by Python (e.g., print(), len(), sum(), type(), etc.)
# 2. User-defined Functions – created by the user using the 'def' keyword

# -------------------------------
# Example of a User-defined Function
# -------------------------------

# Syntax:
# def function_name(parameters):
#     # code block
#     return value


def calc_sum(a, b):
    total = a + b
    return total  # returning the result


# Example usage
result = calc_sum(5, 7)  # calling user-defined function
print("Sum:", result)  # using built-in print function

# ==================================================== #
#                  Recursion in Python                 #
# ==================================================== #

# Recursion means:
# A function calling itself repeatedly until a base condition is met.

# -------------------------------
# Example 1: Print numbers from n to 1 using recursion
# -------------------------------


def print_numbers_desc(n):
    if n == 0:  # base case (stop condition)
        return
    print(n)
    print_numbers_desc(n - 1)  # recursive call


# Example usage
print("Printing from 5 to 1:")
print_numbers_desc(5)

# -------------------------------
# Example 2: Print numbers from 1 to n using recursion
# -------------------------------


def print_numbers_asc(n):
    if n == 0:  # base case
        return
    print_numbers_asc(n - 1)  # recursive call
    print(n)


# Example usage
print("\nPrinting from 1 to 5:")
print_numbers_asc(5)

# ==================================================== #
#         Beginner-Friendly Python Practice            #
# ==================================================== #
# Topics Covered: Functions
# Tip: Try solving them before looking at the solution!

# ======================================================================== #
# 1. Write a program to print the length of a list. (list is the parameter)
# ======================================================================== #

fruits = ["apple", "banana", "cherry", "date", "elderberry"]


def print_length(items):
    print(len(items))


print_length(fruits)


# ======================================================================== #
# 2. Write a program to print the elements of a list in a single line.
# ======================================================================== #

fruit_list = ["apple", "banana", "cherry", "date", "elderberry"]


def print_list_elements(items):
    for item in items:
        print(item, end=" ")


print_list_elements(fruit_list)
print()  # just to move to the next line after printing


# ======================================================================== #
# 3. Write a program to find the factorial of n. (n is the parameter)
# ======================================================================== #


def factorial_of_n(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)


factorial_of_n(5)


# ======================================================================== #
# 4. Write a program to convert USD into PKR.
#    Assume that 1 USD = 283 PKR (usd is the parameter)
# ======================================================================== #


def convert_usd_to_pkr(amount):
    pkr = amount * 283
    print(f"{amount} USD is equal to {pkr} PKR")


usd = int(input("Enter the amount in USD: "))
convert_usd_to_pkr(usd)


# ======================================================================== #
# 5. Write a program to check if a number is ODD or EVEN. (num is parameter)
# ======================================================================== #


def num_checker(num):
    if num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")


num = int(input("Enter a number: "))
num_checker(num)

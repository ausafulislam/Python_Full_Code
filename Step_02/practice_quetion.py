# ==================================================== #
#         Python Practice Questions (Set 2)            #
# ==================================================== #

# NOTE: These are beginner-friendly Python practice questions.
# Try solving each one on your own before looking at the answers.
# Topics Covered: Strings, Slicing, Indexing, String Functions, Conditionals.
# Keep practicing and experimenting!


# ---------------------------------------------------- #
# 1. Write a program to input the user’s first name and print its length.
# ---------------------------------------------------- #

# Explanation:
# len(string) gives the total number of characters in a string.

# Solution:
user_name = input("Enter your First Name: ")
print("Length of your name is:", len(user_name))


# ---------------------------------------------------- #
# 2. Write a program to find the occurrence of ‘$’ in a string entered by the user.
# ---------------------------------------------------- #

# Explanation:
# .count("character") counts how many times a character occurs in the string.

# Solution:
user_input = input("Enter some text: ")
print("Count of '$' in the text is:", user_input.count("$"))


# ---------------------------------------------------- #
# 3. Write a program to check if a number entered by the user is odd or even.
# ---------------------------------------------------- #

# Explanation:
# A number is Even if divisible by 2 (num % 2 == 0).
# Otherwise, it is Odd.

# Solution:
user_num = int(input("Enter a number to check if it is Odd or Even: "))

if user_num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")


# ---------------------------------------------------- #
# 4. Write a program to find the greatest of 3 numbers entered by the user.
# ---------------------------------------------------- #

# Explanation:
# Compare numbers using if-elif-else.
# Check all conditions step by step.

# Solution:
num1 = int(input("Enter the First number: "))
num2 = int(input("Enter the Second number: "))
num3 = int(input("Enter the Third number: "))

if num1 == num2 == num3:
    print("All numbers are equal.")
elif num1 >= num2 and num1 >= num3:
    print("The greatest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The greatest number is:", num2)
else:
    print("The greatest number is:", num3)


# ---------------------------------------------------- #
# 5. Write a program to check if a number is a multiple of 7 or not.
# ---------------------------------------------------- #

# Explanation:
# A number is a multiple of 7 if (num % 7 == 0).

# Solution:
user_input = int(input("Enter a number to check if it is a multiple of 7: "))

if user_input % 7 == 0:
    print("The number is a multiple of 7.")
else:
    print("The number is not a multiple of 7.")

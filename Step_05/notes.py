# ==================================================== #
#                    Loops in Python                   #
# ==================================================== #

# ---------------------------------------------------- #
# while loop in Python
# ---------------------------------------------------- #
# A while loop repeatedly executes a block of code as
# long as a condition is true.
# Useful when the number of iterations is not known beforehand.

# Basic Structure
i = 0
while i < 5:
    print("Hello, World!")
    i += 1  # Increment to avoid infinite loop

# Example: Print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1


# ---------------------------------------------------- #
# break keyword in loop
# ---------------------------------------------------- #
# The 'break' statement is used to exit a loop prematurely.
# It stops the loop even if the condition is still true.

# Example: Print numbers from 1 to 10, but break if number is 5
i = 1
while i <= 10:
    print(i)
    if i == 5:
        print("i is equal to 5, breaking the loop.")
        break
    i += 1


# ==================================================== #
# for loop in Python
# ==================================================== #
# A for loop iterates over a sequence (list, tuple, string, etc.)
# and executes a block of code for each item.
# Commonly used when the number of iterations is known.

# Basic Example: Iterate through a string
text = "hello world"
for ch in text:
    print(ch)


# ---------------------------------------------------- #
# Optional else in for loop
# ---------------------------------------------------- #
# A for loop can have an optional 'else' block that executes
# only if the loop completes normally (not interrupted by break).

# Example: Print numbers from 1 to 5 with an else block
num_list = [1, 2, 3, 4, 5]
for i in num_list:
    print(i)
else:
    print("Loop completed without interruption.")


# ---------------------------------------------------- #
# range() function in loop
# ---------------------------------------------------- #
# The range() function generates a sequence of numbers.
# Syntax: range(start, stop, step)

# Example: Print numbers from 0 to 4
for i in range(5):  # range(stop)
    print(i)

# Example: Print numbers from 1 to 9
for i in range(1, 10):  # range(start, stop)
    print(i)

# Example: Print numbers from 1 to 9 with step 2
for i in range(1, 10, 2):  # range(start, stop, step)
    print(i)

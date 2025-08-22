# ==================================================== #
#                  STRINGS IN PYTHON                  #
# ==================================================== #

# A string is a sequence of characters enclosed in single (' ') or double (" ") quotes.
# Strings are used to store text (words, sentences, symbols).

# Example:
name = "Ausaf"
greeting = "Hello, World!"

# Multiline Strings → Use triple quotes (''' or """)
about = """Ausaf is a
Python developer and
a creative mind."""
print(about)

# ---------------------------------------------------- #
#               STRING INDEXING AND SLICING           #
# ---------------------------------------------------- #

# Each character in a string has an index (starts from 0)
text = "Python"
# Index:     0 1 2 3 4 5
# Characters:P y t h o n

print(text[0])  # Output: 'P'
print(text[-1])  # Output: 'n'

# String Slicing:
print(text[0:3])  # Output: 'Pyt'
print(text[2:])  # Output: 'thon'
print(text[:4])  # Output: 'Pyth'

# ---------------------------------------------------- #
#             STRING FUNCTIONS / METHODS              #
# ---------------------------------------------------- #

msg = "  hello python  "

print(msg.upper())  # '  HELLO PYTHON  '
print(msg.lower())  # '  hello python  '
print(msg.strip())  # 'hello python'
print(msg.replace("python", "world"))  # '  hello world  '
print(len(msg))  # 16
print(msg.startswith("  h"))  # True
print(msg.endswith("n  "))  # True
print(msg.count("l"))  # 2
print(msg.find("h"))  # 2

# ---------------------------------------------------- #
#             F-STRINGS (STRING FORMATTING)           #
# ---------------------------------------------------- #

# f-strings let you embed variables inside a string
name = "Ausaf"
age = 17

print(f"My name is {name} and I am {age} years old.")

# ---------------------------------------------------- #
#           ESCAPE CHARACTERS IN STRINGS              #
# ---------------------------------------------------- #

print('He said, "Hello!"')  # He said, "Hello!"
print("It's a good day.")  # It's a good day.
print("Line1\nLine2")  # Line1
# Line2
print("Tab\tSpace")  # Tab    Space

# ---------------------------------------------------- #
#         EXTRA: STRING BEHAVIOR & IMMUTABILITY       #
# ---------------------------------------------------- #

# 1. .strip() removes extra spaces from both ends
msg = "   Hello Python   "
print(f"Stripped: '{msg.strip()}'")

# 2. .find() returns index or -1
text = "Ausaf is learning Python"
print(text.find("a"))  # 1
print(text.find("x"))  # -1

# 3. Strings are immutable (can't modify characters directly)
name = "Ausaf"
# name[0] = "B"  # ❌ Error
new_name = "B" + name[1:]  # ✅ Correct way
print(new_name)  # Busaf

# ==================================================== #
#         CONDITIONAL STATEMENTS IN PYTHON            #
# ==================================================== #

# Conditional statements are used to make decisions.
# Types: if, if-else, if-elif-else

# --------------------- BASIC SYNTAX ----------------- #
# if condition:
#     # code block

# if condition:
#     # true block
# else:
#     # false block

# if condition1:
#     # block1
# elif condition2:
#     # block2
# else:
#     # fallback

# ------------------ EXAMPLE: if-else ---------------- #
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# -------------- EXAMPLE: if-elif-else -------------- #
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D or below")

# -------------- COMPARISON OPERATORS --------------- #
# ==  Equal to
# !=  Not equal to
# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to

x = 10
print(x == 10)  # True
print(x != 5)  # True

# ==================================================== #
#       NESTED CONDITIONAL STATEMENTS IN PYTHON       #
# ==================================================== #

# Nested means: an if statement inside another if/else block.

# --------------------- SYNTAX ----------------------- #
# if condition1:
#     if condition2:
#         # do something
#     else:
#         # inner else
# else:
#     # outer else

# ------------- EXAMPLE 1: nested if ----------------- #
age = int(input("Enter your age: "))
citizen = input("Are you a citizen of this country? (yes/no): ")

if age >= 18:
    if citizen.lower() == "yes":
        print("You are eligible to vote.")
    else:
        print("You must be a citizen to vote.")
else:
    print("You are not eligible to vote due to age.")

# -------- EXAMPLE 2: nested grading system ---------- #
marks = int(input("Enter your marks: "))

if marks >= 60:
    print("You passed.")
    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    else:
        print("Grade: C")
else:
    print("You failed.")

# ------------------ TIPS FOR NESTED IF -------------- #
# - Use nested if when one condition depends on another
# - Avoid deep nesting (keep it simple and readable)
# - Indentation is very important in nested conditions

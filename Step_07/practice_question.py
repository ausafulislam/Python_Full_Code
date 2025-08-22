# ==================================================== #
#                Python Practice Questions             #
# ==================================================== #
# Note: These are beginner-friendly Python practice questions.
# Try solving each one on your own before looking at the answers.
# Topics Covered: File Input / Output (File Handling)

# -------------------------------------------------------------------------- #
# 1. Create a new file “practice.txt” using Python. Add the following data:
#    Hello, I am learning JavaScript.
#    I am using JavaScript to write a file.
#    This is the sample line.
# -------------------------------------------------------------------------- #

with open("practice.txt", "w") as file:
    file.write("Hello, I am learning JavaScript.\n")
    file.write("I am using JavaScript to write a file.\n")
    file.write("This is the sample line.\n")


# -------------------------------------------------------------------------- #
# 2. Replace all occurrences of “JavaScript” with “Python” in the file.
# -------------------------------------------------------------------------- #

with open("practice.txt", "r") as file:
    data = file.read()

new_data = data.replace("JavaScript", "Python")

with open("practice.txt", "w") as file:
    file.write(new_data)

print("Replaced 'JavaScript' with 'Python'")


# -------------------------------------------------------------------------- #
# 3. Search if the word “learning” exists in the file or not.
# -------------------------------------------------------------------------- #

word = "learning"
with open("practice.txt", "r") as file:
    data = file.read()
    if word in data:
        print("Word found")
    else:
        print("Word not found")


# -------------------------------------------------------------------------- #
# 4. Find in which line the word “learning” occurs first.
#    Print -1 if the word is not found.
# -------------------------------------------------------------------------- #

word = "learning"
line_no = 0
found = False

with open("practice.txt", "r") as file:
    for line in file:
        line_no += 1
        if word in line:
            print(f"Word found at line {line_no}")
            found = True
            break

if not found:
    print("-1")


# -------------------------------------------------------------------------- #
# 5. From a file containing numbers separated by commas,
#    print the count of even numbers.
# -------------------------------------------------------------------------- #

# Example file content: 2,3,4,5,6,7,8
with open("numbers.txt", "w") as file:
    file.write("2,3,4,5,6,7,8")

count = 0
with open("numbers.txt", "r") as file:
    data = file.read()
    nums = data.split(",")
    for val in nums:
        if int(val) % 2 == 0:
            print(val)
            count += 1

print("Count of even numbers:", count)

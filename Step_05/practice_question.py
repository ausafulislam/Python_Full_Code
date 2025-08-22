# ==================================================== #
#             Beginner-Friendly Python Practice        #
# ==================================================== #
# Topics Covered: Loops, For Loop, While Loop
# Tip: Try solving them before looking at the solution!

# ==================================================== #
# 1. Print numbers from 1 to 100
# ==================================================== #

i = 1
while i <= 100:
    print(i)
    i += 1

# ==================================================== #
# 2. Print numbers from 100 to 1
# ==================================================== #

i = 100
while i >= 1:
    print(i)
    i -= 1

# ==================================================== #
# 3. Print the multiplication table of a number (using while loop)
# ==================================================== #

n = int(input("Enter a number to print its multiplication table: "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1

# ==================================================== #
# 4. Print all elements of a list (using while loop)
# ==================================================== #

nums_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums_list):
    print(nums_list[idx])
    idx += 1

# ==================================================== #
# 5. Search for a number in a tuple (using while loop)
# ==================================================== #

nums_tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter a number to search in the tuple: "))
i = 0
found = False

while i < len(nums_tuple):
    if nums_tuple[i] == x:
        print(f"Found at index {i}")
        found = True
        break
    i += 1

if not found:
    print("Not Found")

# ==================================================== #
# 6. Print all elements of a list (using for loop)
# ==================================================== #

nums_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for num in nums_list:
    print(num)

# ==================================================== #
# 7. Search for a number in a tuple (using for loop)
# ==================================================== #

nums_tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 64)
x = 64
idx = 0
for val in nums_tuple:
    if val == x:
        print(f"Found {x} in the tuple at index {idx}")
    idx += 1

# ==================================================== #
# 8. Print the multiplication table of a number (using for loop)
# ==================================================== #

n = int(input("Enter a number to print its multiplication table: "))
for tbl in range(1, 11):
    print(f"{n} x {tbl} = {n * tbl}")

# ==================================================== #
# 9. Find the sum of first N natural numbers (using while loop)
# ==================================================== #

natural_num = int(input("Enter a natural number: "))
i = 1
sum_natural = 0
while i <= natural_num:
    sum_natural += i
    i += 1
print(f"The sum of first {natural_num} natural numbers is: {sum_natural}")

# ==================================================== #
# 10. Find the sum of first N natural numbers (using for loop)
# ==================================================== #

natural_num = int(input("Enter a natural number: "))
sum_natural = 0
for i in range(1, natural_num + 1):
    sum_natural += i
print(f"The sum of first {natural_num} natural numbers is: {sum_natural}")

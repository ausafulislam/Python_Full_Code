# ==================================================== #
#              Python Practice Questions               #
# ==================================================== #

# NOTE: These are beginner-friendly Python practice questions.
# Try solving each one on your own before looking at the answers.
# Topics Covered: tuple, list, indexing in tuple and list,
# functions of list and tuple, difference between tuple and list.

# ---------------------------------------------------- #
# 1. Write a program to ask the user to enter names of
#    their 3 favorite movies & store them in a list.
# ---------------------------------------------------- #

# Solution
movie_name1 = input("Enter your first favorite Movie name: ")
movie_name2 = input("Enter your second favorite Movie name: ")
movie_name3 = input("Enter your third favorite Movie name: ")

movie_lst = [movie_name1, movie_name2, movie_name3]
print("Original list:", movie_lst)

movie_lst.sort()
print("Sorted list:", movie_lst)


# ---------------------------------------------------- #
# 2. Write a program to check if a list contains a
#    palindrome of elements. (Hint: use copy() method)
# ---------------------------------------------------- #

# Solution
lst = [1, "abc", "abc", 1]

copy_lst = lst.copy()
copy_lst.reverse()

if copy_lst == lst:
    print("List is Palindrome")
else:
    print("List is Not Palindrome")


# ---------------------------------------------------- #
# 3. Write a program to count the number of students
#    with the “A” grade in the following tuple.
# ---------------------------------------------------- #

# Solution
student_grade = (
    "A",
    "B",
    "C",
    "A",
    "D",
    "E",
    "B",
    "A",
    "A",
    "B",
    "C",
    "A",
    "D",
    "E",
    "B",
    "A",
)

print("Count of A grade:", student_grade.count("A"))


# ---------------------------------------------------- #
# 4. Write a program to store the above values in a list
#    & sort them from “A” to “E”.
# ---------------------------------------------------- #

# Solution
grade = ["A", "B", "C", "A", "D", "E", "B", "A", "A", "B", "C", "A", "D", "E", "B", "A"]
grade.sort()
print("Sorted grades list:", grade)

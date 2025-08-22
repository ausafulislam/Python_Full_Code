# ==================================================== #
#               Python Practice Questions              #
# ==================================================== #
# NOTE: These are beginner-friendly Python practice questions.
# Try solving each one on your own before looking at the answers.
# Topics Covered: Sets and Dictionary
# ==================================================== #

# ---------------------------------------------------- #
# 1. Store Word Meanings in a Dictionary
# ---------------------------------------------------- #
# table has two meanings:
#   "a piece of furniture"
#   "list of facts & figures"
# cat has one meaning:
#   "a small animal"

# Solution
word_meaning = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat": "a small animal",
}
print("Word Meanings Dictionary:", word_meaning)


# ---------------------------------------------------- #
# 2. Find Number of Classrooms Required
# ---------------------------------------------------- #
# You are given a list of subjects. Assume one classroom
# is required for 1 subject. How many classrooms are needed?

# Subjects:
# "python", "java", "C++", "python", "javascript",
# "java", "python", "java", "C", "C++"

# Solution
subject_set = {
    "python",
    "java",
    "C++",
    "python",
    "javascript",
    "java",
    "python",
    "java",
    "C",
    "C++",
}
print("Classrooms Needed:", len(subject_set))


# ---------------------------------------------------- #
# 3. Store Marks of 3 Subjects in a Dictionary
# ---------------------------------------------------- #
# Write a program to take marks of 3 subjects from the user.
# Store them in a dictionary with subject name as key & marks as value.

# Solution
marks_dict = {}

marks1 = int(input("Enter marks for Physics: "))
marks_dict.update({"Physics": marks1})

marks2 = int(input("Enter marks for Chemistry: "))
marks_dict.update({"Chemistry": marks2})

marks3 = int(input("Enter marks for Mathematics: "))
marks_dict.update({"Mathematics": marks3})

print("\nMarks Dictionary:", marks_dict)


# ---------------------------------------------------- #
# 4. Store 9 and 9.0 as Separate Values in a Set
# ---------------------------------------------------- #
# (Hint: Use built-in data types like str along with int/float)

# Solution
my_set = {9, "9.0"}
print("Set with Separate Values:", my_set)

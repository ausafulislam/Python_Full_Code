# ==================================================== #
#              Dictionary & Sets in Python             #
# ==================================================== #

# -------------------------------
# Dictionary in Python
# -------------------------------
# - A dictionary is a collection of key-value pairs.
# - Keys must be unique and immutable (e.g., str, int, tuple).
# - Values can be any data type.
# - Provides fast lookups, ideal for structured data.

# Creating a Dictionary
my_dict = {"name": "Ausaf", "age": 25, "language": "Python"}

# Accessing Values
print(my_dict["name"])  # Output: Ausaf
print(my_dict.get("age"))  # Output: 25

# Adding or Updating Items
my_dict["country"] = "Pakistan"  # Adds new key
my_dict["age"] = 26  # Updates existing key

# Dictionary Methods
print(my_dict.keys())  # dict_keys(['name', 'age', 'language', 'country'])
print(my_dict.values())  # dict_values(['Ausaf', 26, 'Python', 'Pakistan'])
print(my_dict.items())  # dict_items([...])
print(my_dict.get("name", "Not Found"))  # Output: Ausaf

# Updating with another dictionary
my_dict.update({"name_1": "afaq", "name_2": "imad"})
print(my_dict)

# Nesting Dictionaries
students = {
    "student1": {"name": "Ali", "age": 20},
    "student2": {"name": "Sara", "age": 22},
}
print(students["student1"]["name"])  # Output: Ali


# -------------------------------
# Set in Python
# -------------------------------
# - A set is an unordered collection of unique elements.
# - Duplicate values are not allowed.
# - Useful for mathematical operations and membership tests.

# Creating a Set
my_set = {1, 2, 3, 4, 5}
print(my_set)

# Creating an Empty Set
empty_set = set()
print(empty_set)

# Adding Elements
empty_set.add(1)
empty_set.add(2)
empty_set.add(3)
print(empty_set)

# Removing Random Element
empty_set.pop()
print(empty_set)

# Clearing the Set
empty_set.clear()
print(empty_set)

# Removing Specific Elements
my_set.remove(3)  # Removes 3, error if not found
my_set.discard(10)  # Safe remove, no error if not found
print(my_set)

# Set Utility Methods
print(len(my_set))  # 4
print(4 in my_set)  # True

# Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union: All unique elements
print(set1 | set2)  # {1, 2, 3, 4, 5}
print(set1.union(set2))

# Intersection: Common elements
print(set1 & set2)  # {3}
print(set1.intersection(set2))

# Difference: Elements in set1 not in set2
print(set1 - set2)  # {1, 2}
print(set1.difference(set2))

# Symmetric Difference: Elements in either set but not both
print(set1 ^ set2)  # {1, 2, 4, 5}
print(set1.symmetric_difference(set2))

# Set ignores duplicates
duplicate_set = {1, 2, 2, 3, 3, 4}
print(duplicate_set)  # {1, 2, 3, 4}

# Empty Set vs Empty Dictionary
empty_set = set()  # Creates empty set
empty_dict = {}  # Creates empty dictionary


# -------------------------------
# Summary: Dictionary vs Set
# -------------------------------
# Dictionary:
#   - Structure: {key: value}
#   - Keys must be unique
#   - Fast key-based access
#   - Use case: Storing and mapping related data
#
# Set:
#   - Structure: {value1, value2, ...}
#   - All values must be unique
#   - Use case: Membership tests, set operations, removing duplicates

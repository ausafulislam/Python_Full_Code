# ==================================================== #
#                  Lists in Python                     #
# ==================================================== #

# What is a List?
# A List is a collection of multiple values stored in a single variable.
# Lists are ordered, mutable (changeable), and can contain different data types.

# Creating a List:
fruits = ["Apple", "Banana", "Mango", "Orange"]
print("My Fruits List:", fruits)
# Output: ['Apple', 'Banana', 'Mango', 'Orange']

# A List can contain numbers, strings, or mixed types
mixed = [10, "Python", 3.14, True]
print("Mixed List:", mixed)
# Output: [10, 'Python', 3.14, True]

# Indexing (Accessing Elements)
print("First fruit:", fruits[0])
# Output: Apple
print("Last fruit:", fruits[-1])
# Output: Orange

# Slicing (Getting a portion of the list)
print("First 2 fruits:", fruits[0:2])
# Output: ['Apple', 'Banana']

# Changing List Elements (Lists are mutable)
fruits[1] = "Kiwi"
print("Updated Fruits List:", fruits)
# Output: ['Apple', 'Kiwi', 'Mango', 'Orange']

# Adding Elements
fruits.append("Grapes")  # Adds to end
print("After append:", fruits)
# Output: ['Apple', 'Kiwi', 'Mango', 'Orange', 'Grapes']

fruits.insert(2, "Pineapple")  # Adds at index 2
print("After insert:", fruits)
# Output: ['Apple', 'Kiwi', 'Pineapple', 'Mango', 'Orange', 'Grapes']

# Removing Elements
fruits.remove("Kiwi")  # Removes "Kiwi"
print("After remove:", fruits)
# Output: ['Apple', 'Pineapple', 'Mango', 'Orange', 'Grapes']

popped_item = fruits.pop()  # Removes last item
print("After pop:", fruits)
# Output: ['Apple', 'Pineapple', 'Mango', 'Orange']
print("Popped item was:", popped_item)
# Output: Grapes

# List Length
print("Total items in list:", len(fruits))
# Output: 4

# Sorting a List
numbers = [4, 2, 9, 1, 5]
numbers.sort()
print("Sorted numbers:", numbers)
# Output: [1, 2, 4, 5, 9]

# Reversing a List
numbers.reverse()
print("Reversed numbers:", numbers)
# Output: [9, 5, 4, 2, 1]

# Copying a List
copied_list = fruits.copy()
print("Copied Fruits List:", copied_list)
# Output: ['Apple', 'Pineapple', 'Mango', 'Orange']

# Clearing a List
copied_list.clear()
print("Cleared List:", copied_list)
# Output: []


# ==================================================== #
#                  Tuples in Python                    #
# ==================================================== #

# What is a Tuple?
# A Tuple is a collection of ordered, immutable elements.
# Once created, the elements of a tuple cannot be changed.
# Tuples are defined using parentheses ().

# Creating Tuples
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

tuple2 = "red", "green", "blue"  # Without parentheses
print(tuple2)

one_element = ("alone",)  # Single-element tuple
print(type(one_element))  # Output: <class 'tuple'>

# Accessing Tuple Elements
print(my_tuple[0])  # Output: apple
print(my_tuple[-1])  # Output: cherry

# Tuple Slicing
print(my_tuple[0:2])  # Output: ('apple', 'banana')
print(my_tuple[1:])  # Output: ('banana', 'cherry')

# Tuple Methods
print(my_tuple.count("apple"))  # Output: 1
print(my_tuple.index("banana"))  # Output: 1

# Tuples Are Immutable
# my_tuple[0] = "grape"  ❌ This will cause an error!
new_tuple = ("grape",) + my_tuple[1:]
print(new_tuple)  # Output: ('grape', 'banana', 'cherry')

# Tuple with Different Data Types
mixed = (1, "hello", 3.14, True)
print(mixed)

# Tuple Unpacking
person = ("Ausaf", 23, "Python Developer")
name, age, profession = person
print(name)
print(age)
print(profession)

# Why Use Tuples?
# - Tuples use less memory than lists
# - Tuples can be used as keys in dictionaries
# - Useful when data should not change

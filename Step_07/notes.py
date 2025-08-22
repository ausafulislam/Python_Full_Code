# ====================================================
#           File Input & Output in Python
# ====================================================

# Opening a file in Python:
# Syntax: open(filename, mode)
# Common modes:
# 'r'   -> Read (default, file must exist)
# 'w'   -> Write (creates or overwrites file)
# 'a'   -> Append (adds data to the end)
# 'x'   -> Create (fails if file already exists)
# 'b'   -> Binary mode (e.g., 'rb', 'wb') for non-text files
# 't'   -> Text mode (default, e.g., 'rt', 'wt')
# '+'   -> Read and write (e.g., 'r+', 'w+', 'a+')

# ====================================================
# Example: 'r' mode (Read) — file must exist
file = open("demo.txt", "r")
print("Reading with 'r' mode:")
print(file.read())
file.close()

# ====================================================
# Example: 'w' mode (Write) — creates or overwrites file
file = open("demo_write.txt", "w")
file.write("This is written with 'w' mode.\n")
file.write("Old content (if any) is replaced.")
file.close()

# ====================================================
# Example: 'a' mode (Append) — adds to the end of the file
file = open("demo_write.txt", "a")
file.write("\nThis line is added using 'a' mode.")
file.close()

# ====================================================
# Example: 'x' mode (Exclusive creation) — fails if file exists
try:
    file = open("newfile.txt", "x")
    file.write("File created with 'x' mode.")
    file.close()
except FileExistsError:
    print("File already exists!")

# ====================================================
# Example: 'b' mode (Binary)
# Writing a binary file
with open("binary_demo.bin", "wb") as file:
    file.write(b"\x48\x65\x6c\x6c\x6f")  # "Hello" in hex

# Reading a binary file
with open("binary_demo.bin", "rb") as file:
    data = file.read()
    print("\nBinary file content:", data)

# ====================================================
# Example: 'r+' mode (Read and write without truncating)
file = open("demo_write.txt", "r+")
content = file.read()
print("\n'r+' mode content before writing:")
print(content)
file.write("\nAdded this line using 'r+' mode.")
file.close()

# ====================================================
# Best Practice: Using 'with' in File Handling
# ----------------------------------------------------
# What is 'with'?
# 'with' is a context manager in Python.
# It automatically opens and closes the file for you.
# Even if an error occurs inside the block, the file will be closed.
#
# Advantages:
# 1. No need to call file.close() manually.
# 2. Prevents resource leaks.
# 3. Code is cleaner and more readable.

# Example: Reading a file using 'with'
with open("demo.txt", "r") as f:
    print("\nUsing 'with' statement for reading:")
    print(f.read())

# Example: Writing to a file using 'with'
with open("demo_with.txt", "w") as f:
    f.write("This file was written using the 'with' statement.\n")
    f.write("No need to manually close the file!")

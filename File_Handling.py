# FILE HANDLING 
import os

filename = "sample.txt"

# 1. CREATE & WRITE FILE
with open(filename, "w") as file:
    file.write("Hello Python\n")
    file.write("Welcome to File Handling\n")

print("File created and data written.\n")

# 2. READ ENTIRE FILE
print("Reading full file:\n")

with open(filename, "r") as file:
    content = file.read()
    print(content)

# 3. APPEND DATA
with open(filename, "a") as file:
    file.write("This line is appended.\n")

print("\nData appended successfully.\n")

# 4. READ LINE BY LINE
print("Reading line by line:\n")

with open(filename, "r") as file:
    for line in file:
        print(line.strip())

# 5. READ ONE LINE
print("\nReading first line only:\n")

with open(filename, "r") as file:
    print(file.readline())

# 7. CHECK FILE EXISTS
print("\nChecking file existence:")

if os.path.exists(filename):
    print("File exists.")
else:
    print("File does not exist.")

# 9. ERROR HANDLING
print("\nException Handling Example:")

try:
    with open("unknown.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: File not found.")

# 10. DELETE FILE
choice = input("\nDo you want to delete the files? (yes/no): ")

if choice.lower() == "yes":
    os.remove(filename)
    print("Files deleted successfully.")
else:
    print("Files kept safely.")

print("\nProgram completed.")
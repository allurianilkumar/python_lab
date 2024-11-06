# array_operations.py
# Importing the array module
from array import array
# Initialize an array of integers
arr = array("i", [1, 2, 3, 4, 5])
# Function to display the array
def display_array():
    print("Array:", arr.tolist())
# Function to append an item to the array
def append_item(item):
    arr.append(item)
    print(f"Appended {item} to the array.")
# Function to insert an item at a specific position
def insert_item(index, item):
    arr.insert(index, item)
    print(f"Inserted {item} at index {index}.")
# Function to reverse the array
def reverse_array():
    arr.reverse()
    print("Reversed the array.")
# Demonstrate functionality
print("Initial array:")
display_array()
# Append an item
append_item(6)
display_array()
# Insert an item
insert_item(2, 9)
display_array()
# Reverse the array
reverse_array()
display_array()

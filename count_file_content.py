# count_file_content.py

# Open the file for reading
with open("source.txt", "r") as file:
    text = file.read()

# Count characters
num_chars = len(text)

# Count words
num_words = len(text.split())

# Count lines
num_lines = text.count("\n") + 1 if text else 0

print("Number of characters:", num_chars)
print("Number of words:", num_words)
print("Number of lines:", num_lines)

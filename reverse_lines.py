# reverse_lines.py

# Open and read the file
with open("source.txt", "r") as file:
    # Read each line and print in reverse
    for line in file:
        print(line.strip()[::-1])

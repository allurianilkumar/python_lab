# Read words from the source file
with open("source.txt", "r") as src:
    words = src.read().split()

# Sort words, convert to lowercase
sorted_words = sorted(word.lower() for word in words)

# Write sorted words to the output file
with open("output.txt", "w") as out:
    out.write("\n".join(sorted_words))

print("Words have been sorted and saved in 'output.txt'")

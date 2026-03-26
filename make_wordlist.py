import re

with open("BeeMovie.txt", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Extract words using a findall text for only alphanumeric characters
words = re.findall(r'[A-Za-z0-9]+', text)

#Remove Duplicates For-loop
seen = set()
unique_words = []
for word in words:
    if word not in seen:
        seen.add(word)
        unique_words.append(word)

# Write unique words to wordlist.txt using a with statement to ensure the file is properly closed
with open("wordlist.txt", "w") as f:
    f.write("\n".join(unique_words) + "\n")

print(f"Done! {len(unique_words)} unique words written to wordlist.txt")

#how it works
#1 

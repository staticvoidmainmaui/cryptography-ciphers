import hashlib
import sys
import re

#---------------- STEP 1-  Encode the String in UTF8 , didnt completely understand process but I know it converts the string into bytes which is required for hashing functions ------

def custom_hash(password):
    data = password.encode('utf-8')
    for _ in range(100):
        data = hashlib.md5(data).digest()
    for _ in range(100):
        data = hashlib.sha256(data).digest()
    for _ in range(100):
        data = hashlib.sha512(data).digest()
    return data.hex()

#----------------- STEP 2-  Read the wordlist and check each word against the target hash ---------------------------------------
def crack(target_hash, wordlist_file):
    with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            word = line.strip()
            # Only try 6-character alphanumeric words, using A-z, z0-9, and 0-9, using regex to ensure we only check valid candidates
            if len(word) == 6 and re.fullmatch(r'[A-Za-z0-9]+', word):
                if custom_hash(word) == target_hash:
                    print(f"Password found: {word}")
                    return
    print("Password not found in wordlist.")

#----------------- STEP 3-  Main function to run the script with command line arguments ---------------------------------------

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python crack_custom.py <hash> <wordlist>")
        sys.exit(1)

    crack(sys.argv[1], sys.argv[2])

#!/usr/bin/env python3
import hashlib
import sys
import re

#SHA512( SHA512( ( SHA256( SHA256( ( MD5( MD5( ( " string" )  ... )


#------------- STEP 1-  Custom Hash Function Implementation ---------------------------------------
# #HASHMODE: python custom_hash.py <password>

def custom_hash(password):
    # UTF-8 encode the input string
    data = password.encode('utf-8')

    # 100 rounds of MD5 
    for _ in range(100):
        data = hashlib.md5(data).digest()

    # 100 rounds of SHA256 
    for _ in range(100):
        data = hashlib.sha256(data).digest()

    # 100 rounds of SHA512
    for _ in range(100):
        data = hashlib.sha512(data).digest()
    # Return final result as hexadecimal string
    return data.hex()

#----------------- STEP 2-  Read the wordlist and check each word against the target hash ---------------------------------------
#CRACKMODE: python custom_hash.py <hash> <wordlist>

def crack(target_hash, wordlist_file):
    with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            word = line.strip()
            # Only try 6-character alphanumeric words using regex to ensure we only check valid candidates
            if len(word) == 6 and re.fullmatch(r'[A-Za-z0-9]+', word):
                if custom_hash(word) == target_hash:
                    print(f"Password found: {word}")
                    return
    print("Password not found in wordlist.")

#----------------- STEP 3-  Main function to run the script with command line arguments ---------------------------------------
if __name__ == "__main__":

    if len(sys.argv) == 2:
        arg = sys.argv[1]
        # If argument is 128 hex characters, it's a hash — run crack mode with hardcoded wordlist
        if len(arg) == 128 and re.fullmatch(r'[0-9a-f]+', arg):
            crack(arg, 'rockyou-20.txt')
        # Otherwise treat it as a password and hash it
        else:
            print(custom_hash(arg))
    else:
        print("Usage:")
        print("  Hash a password:  ./crack_hashes <password>")
        print("  Crack a hash:     ./crack_hashes <hash>")
        sys.exit(1)

# CIPHERS 

A collection of cryptographic attack implementations demonstrating core cybersecurity concepts including hash cracking, dictionary attacks, and classical cipher breaking.

## Project Overview

This repository implements practical cryptanalysis techniques to show proficiency in:
- **Hash function analysis**
- **Dictionary attacks**
- **Cryptanalysis** 

All implementations are educational and for authorized security testing purposes only.

---

## 📁 Project Structure

### **Hash Ciphers** (`hash_ciphers/`)
Demonstrates hash function implementation and cracking techniques.

#### `custom_cipher/crack_hashes.py`
- **Implements a custom multi-round hash function** combining MD5 (100 rounds) → SHA256 (100 rounds) → SHA512 (100 rounds)
- **Features:**
  - Hash generation mode: `python crack_hashes.py <password>`
  - Crack mode: `python crack_hashes.py <hash>`
  - Dictionary attack using filtered wordlist (6-char alphanumeric passwords)
  - Regex validation to target specific password patterns

#### Hash Files
- `MD5Crypt_hash.txt` – MD5 crypt examples
- `DESCrypt_hash.txt` – DES crypt examples
- `bcrypt_hash.txt` – Bcrypt hash examples
- `rockyou-20.txt` – Filtered wordlist for cracking

---

### **Vigenere Cipher * (`Vignere Cipher/`)

#### `v_cipher.py`
A complete Vigenere cipher cryptanalysis toolkit implementing multiple attack methods:

**Core Functions:**
- `index_of_coincidence()` – Measures statistical randomness to identify key length
- `score_text()` – Chi-squared test comparing text to English letter frequency distribution
- `find_key_length()` – Determines cipher key length using IC analysis
- `vigenere_decrypt()` – Decrypts ciphertext with given key
- `find_key()` – Attempts to recover the key using frequency analysis

**Attack Method:**
- OPTION 1 : Brute forces all possible key combinations (length 1-4)
- OPTION 2: Scores each result using chi-squared frequency analysis against English text , Returns top 50 candidates ranked by likelihood, Demonstrates that noise in short texts can affect exact key recovery

---

## TO RUN: 

### Cracking Hashes
```bash
# Generate a hash from a password
python hash_ciphers/custom_cipher/crack_hashes.py "password"

# Crack a hash using dictionary attack
python hash_ciphers/custom_cipher/crack_hashes.py "5d41402abc4b2a76b9719d911017c592..."
```

### Decrypting Vigenere Ciphers
```bash
# Interactive decryption with cryptanalysis
python "Vignere Cipher/v_cipher.py"
# Enter ciphertext, receives top 50 key candidates
```
## Requirements

- Python 3.x
- Standard library only (hashlib, sys, re, string)
- John the Ripper Decryption Tool

---

## Technical Concepts Demonstrated

| Technique | Implementation |
|-----------|-----------------|
| **Dictionary Attack** | Wordlist filtering + hash comparison |
| **Frequency Analysis** | Chi-squared statistical test against English letter distribution |
| **Index of Coincidence** | Key length detection for polyalphabetic ciphers |
| **Brute Force** | Exhaustive key space search with scoring |
| **Data Processing** | Regex extraction, deduplication, text cleaning |

---

## 📚 Educational Context

This project is designed for:
- Understanding cryptographic vulnerabilities
- Learning attack methodology and tools
- Practicing python implementation of security concepts
- Preparing for CTF competitions and penetration testing


---

## Additional TOPICS: 

- [ ] GPU acceleration for hash cracking
- [ ] Additional hash algorithm support (bcrypt, scrypt, argon2)
- [ ] Rainbow table implementation
- [ ] Substitution cipher analysis tools

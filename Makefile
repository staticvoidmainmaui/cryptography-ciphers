all:
	cp crack_hashes.py crack_hashes
	chmod +x crack_hashes

hash: all
	./crack_hashes $(PASSWORD)

crack: all
	./crack_hashes $(HASH) rockyou-20.txt

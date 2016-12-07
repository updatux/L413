import random, getpass, hashlib, sys, string

"""
Name    : L413 (precursor of Jcrypt)
Version : 1.0
Type    : Cryptage
Author  : Updatux (0v3rl0w)
"""

def encrypt(text):
	final = ""
	password = getpass.getpass(prompt="Password:")
	hexpass = hashlib.sha512(password).hexdigest()
	hextext = text.encode("hex")
	decipass = int(hexpass, 16)
	decitext = int(hextext, 16)
	code = 0 + decipass + decitext
	for i in range(len(str(code))):
		final += random.choice(string.digits)

	code += int(final)
	print("Text Crypter: \n" + hex(code)[:len(hex(code)) - 1] + "\n")
	print("Cle de Decryptage: \n" + hex(int(final))[:len(hex(int(final))) - 1] + "\n")

def decrypt(text, key):
	password = getpass.getpass(prompt="Password:")
	hexpass = hashlib.sha512(password).hexdigest()
	decipass = int(hexpass, 16)
	decitext = int(text, 16)
	decikey = int(key, 16)
	decitext -= decikey
	decitext -= decipass
	a = "" + hex(decitext)[2:len(hex(decitext)) - 1]
	print(a.decode("hex"))

if __name__ == "__main__":
	if sys.argv[1] == "-e":
		encrypt(" ".join(sys.argv[2:]))

	if sys.argv[1] == "-d":
		decrypt(sys.argv[2], sys.argv[3])

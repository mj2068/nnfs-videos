import hashlib

inputFile = input("input file path: ")
openedFile = open(inputFile)
readFile = openedFile.read()

md5Hash = hashlib.md5(readFile.encode())
md5Hashed = md5Hash.hexdigest()

sha1Hash = hashlib.sha1(readFile.encode())
sha1Hashed = sha1Hash.hexdigest()

print("File name: %s" % inputFile)
print("MD5: %r" % md5Hashed)
print("SHA1: %r" % sha1Hashed)

import hashlib

myPassword=input('')
myHash= hashlib.sha256(myPassword.encode('utf-8')).hexdigest()
print(myHash)
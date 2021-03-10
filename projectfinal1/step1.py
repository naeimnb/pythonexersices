import csv
import hashlib


# define  hashing function
def hashin(myPassword):
    myHash= hashlib.sha256(myPassword.encode('utf-8')).hexdigest()
    return(myHash)

# print(hashin(input('')))

# define rading csv file




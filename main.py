
import string
from random import *


#print(string.punctuation)

#print(string.ascii_letters)

#print(string.digits)

def main():
    characters = string.ascii_letters + string.punctuation + string.digits
    randomkey = "".join(choice(characters)
    for x in range(randint(16, 24)))
    print(randomkey)
    print(len(randomkey))


if __name__ == "__main__":
    main();
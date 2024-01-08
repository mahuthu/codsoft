import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("welcome to password generator")
print("enter the length of password you want")
length = int(input())
print("your password is")
print(generate_password(length))




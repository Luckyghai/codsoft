import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

length = int(input("Enter the length of the password: "))
print("Generated password is:", generate_password(length))

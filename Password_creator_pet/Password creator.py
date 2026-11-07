import random # imported the random module
import string # imported the string module for letters, digits, and punctuation

username = input("Enter your username: ")
print(f"Hello, {username}!")

while True:
    length = int(input("Enter desired password length: "))

    if length < 8:
        print("WARNING!!! Your password is too short! Password length must be at least 8 characters!")
    elif 8 <= length <= 12:
        print("Not bad, cowboy! That'll do.")
        print(f"Great, creating a password of {length} characters!")
        break
    else:
        print("Now that's a heavy-duty one!")
        print(f"Great, creating a password of {length} characters!")
        break

symbols = string.ascii_letters
digits = string.digits  
symbols_special = string.punctuation
all_chars = symbols + digits + symbols_special # combined all character sets into one

password = "" # created an empty string to store the password
for pw in range(length):
    password += random.choice(all_chars)

print(f"Your new password: {password}")
import random

LOWER_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "1234567890"
SPECIAL = "~!@#$%^&*()_+"
ALL_CHARS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL

def generatePassword(length):
    if length < 12:
        difference = 12 - length
        length += difference
    else:
        pass

    password = []
    for char in range(length):
        char = random.choice(ALL_CHARS)
        password.append(char)
    #print(str(password))
    print("".join(password))
    return "".join(password)

assert len(generatePassword(8)) == 12
generatePassword(20)
pw = generatePassword(14)
assert len(pw) == 14
hasLowercase = False
hasUppercase = False
hasNumber = False
hasSpecial = False
for character in pw:
    if character in LOWER_LETTERS:
        hasLowercase = True
    if character in UPPER_LETTERS:
        hasUppercase = True
    if character in NUMBERS:
        hasNumber = True
    if character in SPECIAL:
        hasSpecial = True
assert hasLowercase and hasUppercase and hasNumber and hasSpecial

print("The assert statements passed sucessfully!")
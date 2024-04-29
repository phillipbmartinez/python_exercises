import random

LOWER_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "1234567890"
SPECIAL = "~!@#$%^&*()_+"
all_chars = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL
password = []

def generatePassword(length):
    if length < 12:
        length = 12
    else:
        length = length

    for _ in range(length):
        password.append(random.choice(all_chars))
    random.shuffle(password)
    return password


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
print()
print("All tests passed.")
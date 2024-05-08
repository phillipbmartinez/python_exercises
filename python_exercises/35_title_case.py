def getTitleCase(text):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    titledText = ""
    
    for char in range(len(text)):
        if char == 0:
            # titledText.append(text[char].upper())
            titledText += text[char].upper()
        elif text[char - 1] not in letters:
            titledText += text[char].upper()
        else:
            titledText += text[char].lower()
            # titledText.append(text[char].lower())
    # print(titledText)
    return titledText

# getTitleCase("hello, world!")

assert getTitleCase('Hello, world!') == 'Hello, World!'
assert getTitleCase('HELLO') == 'Hello'
assert getTitleCase('hello') == 'Hello'
assert getTitleCase('hElLo') == 'Hello'
assert getTitleCase('') == ''
assert getTitleCase('abc123xyz') == 'Abc123Xyz'
assert getTitleCase('cat dog RAT') == 'Cat Dog Rat'
assert getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat'

import random
random.seed(42)
chars = list('abcdefghijklmnopqrstuvwxyz1234567890 ,.')
for i in range(1000):
    random.shuffle(chars)
    assert getTitleCase(''.join(chars)) == ''.join(chars).title()
print("All tests passed.")
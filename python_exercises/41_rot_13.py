def rot13(text):
    encryptedText = []
    for i in text:
        if (i.isalpha()) == False:
            encryptedText.append(i)
        if i.isupper() == True:
            if (ord(i) + 13) > 90:
                encrypted_char = (ord(i) + 13) - 26
                encryptedText.append(chr(encrypted_char))
            else:
                encrypted_char = ord(i) + 13
                encryptedText.append(chr(encrypted_char))

        if i.islower() == True:
            if (ord(i) + 13) > 122:
                encrypted_char = (ord(i) + 13) - 26
                encryptedText.append(chr(encrypted_char))
            else:
                encrypted_char = ord(i) + 13
                encryptedText.append(chr(encrypted_char))
    return "".join(encryptedText)

assert rot13('Hello, world!') == 'Uryyb, jbeyq!'
assert rot13('Uryyb, jbeyq!') == 'Hello, world!'
assert rot13(rot13('Hello, world!')) == 'Hello, world!'
assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'
assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'
print("All tests passed.")
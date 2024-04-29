def ASCIITable():
    for num in range(32, 126 + 1):
        print(ord(chr(num)), chr(num))

ASCIITable()
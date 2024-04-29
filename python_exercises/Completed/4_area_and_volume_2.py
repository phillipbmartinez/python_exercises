def area(length, width):
    return length * width

def perimeter(length, width):
    return  length + width + length + width

def volume(length, width, height):
    return length * width * height

def surfaceArea(length, width, height):
    return (length * width * 2) + (length * height * 2) + (width * height * 2)

assert area(10, 10) == 100
assert area(0, 9999) == 0
assert area(5, 8) == 40
assert perimeter(10, 10) == 40
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000
assert volume(9999, 0, 9999) == 0
assert volume(5, 8, 10) == 400
assert surfaceArea(10, 10, 10) == 600
assert surfaceArea(9999, 0, 9999) == 199960002
assert surfaceArea(5, 8, 10) == 340

print(area(10, 10))
print(area(0, 9999))
print(area(5, 8))
print(perimeter(10, 10))
print(perimeter(0, 9999))
print(perimeter(5, 8))
print(volume(10, 10, 10))
print(volume(9999, 0, 9999))
print(volume(5, 8, 10))
print(surfaceArea(10, 10, 10))
print(surfaceArea(9999, 0, 9999))
print(surfaceArea(5, 8, 10))
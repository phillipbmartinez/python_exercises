def drawPyramid(height):
    for rowNumber in range(0, height):
        print(((height - (rowNumber + 1)) * " ") + (rowNumber * 2 + 1) * "#")

drawPyramid(3)
drawPyramid(8)
drawPyramid(30)

print("Hello")
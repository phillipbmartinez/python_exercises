def drawRectangle(width, height):
    if width == 0 or width < 0:
        print("Width value not acceptable.")
    
    if height == 0 or height < 0:
        print("Height value not acceptable")

    for _ in range(height):
        for _ in range(width):
            print("#", end="")
        print()

drawRectangle(10, 4)
print()
drawRectangle(8, 4)
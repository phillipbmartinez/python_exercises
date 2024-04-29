def getSmallest(numbers):
    if numbers == []:
        print("This is an empty list.")
        return None
    
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
             smallest = num
        else:
             smallest = smallest
    print(f"For the list: {numbers}, the smallest number is: {smallest}")
    return smallest


def getBiggest(numbers):
    if numbers == []:
        print("This is an empty list.")
        return None
    
    biggest = numbers[0]
    for num in numbers:
        if num > biggest:
             biggest = num
        else:
             biggest = biggest
    print(f"For the list: {numbers}, the biggest number is: {biggest}")
    return biggest

getSmallest([1, 2, 3])
getSmallest([3, 2, 1])
getSmallest([28, 25, 42, 2, 28])
getSmallest([1])
getSmallest([])

getBiggest([1, 2, 3])
getBiggest([3, 2, 1])
getBiggest([28, 25, 42, 2, 28])
getBiggest([1])
getBiggest([])

# assert getSmallest([1, 2, 3]) == 1
# assert getSmallest([3, 2, 1]) == 1
# assert getSmallest([28, 25, 42, 2, 28]) == 2
# assert getSmallest([1]) == 1
# assert getSmallest([]) == None
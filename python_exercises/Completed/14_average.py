def average(numbers):
    if len(numbers) == 0:
        print("None")
        return None
    
    calc_sum = 0
    for num in numbers:
        calc_sum += num
    
    average = calc_sum/(len(numbers))
    #print(int(average))
    return int(average)

# average([1, 2, 3])
# average([1, 2, 3, 1, 2, 3, 1, 2, 3])
# average([12, 20, 37])
# average([0, 0, 0, 0, 0])

assert average([1, 2, 3]) == 2
assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
assert average([12, 20, 37]) == 23
assert average([0, 0, 0, 0, 0]) == 0
import random
random.seed(42)
testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]
for i in range(1000):
    random.shuffle(testData)
    assert average(testData) == 2
def mode(numbers):
    dict = {}
    most_freq_num = 0
    most_freq_num_count = 0

    if len(numbers) == 0:
        #print("None")
        return None
    
    for num in numbers:
        if num not in dict:
            dict[num] = 0
        dict[num] += 1

        if dict[num] > most_freq_num_count:
            most_freq_num = num
            most_freq_num_count = dict[num]
    return most_freq_num
#     print(numbers)        
#     print(dict)
#     print(most_freq_num)

# mode([])
# mode([1, 2, 3, 4, 4])
# mode([1, 1, 2, 3, 4])

assert mode([]) == None
assert mode([1, 2, 3, 4, 4]) == 4
assert mode([1, 1, 2, 3, 4]) == 1

import random
random.seed(42)
testData = [1, 2, 3, 4, 4]
for i in range(1000):
    random.shuffle(testData)
    assert mode(testData) == 4
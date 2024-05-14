def collatz(startingNumber):
    if startingNumber < 1:
        return []
    
    num = startingNumber
    sequence = [num]
    while num != 1:
        if num % 2 == 0:
            num = num / 2
            sequence.append(int(num))
        elif num % 2 != 0:
            num = 3*num + 1
            sequence.append(int(num))
        elif num == 1:
            break
        else:
            break
    # print(sequence)
    return sequence

# collatz(10)
# collatz(11)


assert collatz(0) == []
assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
assert len(collatz(256)) == 9
assert len(collatz(257)) == 123
import random
random.seed(42)
for i in range(1000):
    startingNum = random.randint(1, 10000)
    seq = collatz(startingNum)
    assert seq[0] == startingNum # Make sure it includes the starting number.
    assert seq[-1] == 1  # Make sure the last integer is 1.
print("All tests passed.")
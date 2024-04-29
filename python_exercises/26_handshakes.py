def printHandshakes(people):
    if len(people) == 0:
        return None
    
    num_of_hand_shakes = []
    for i in range(0, len(people)):
        for j in range(i + 1, len(people)):
            if i == j:
                pass
            else:
                num_of_hand_shakes.append(f"{people[i]} shakes hands with {people[j]}")
    # for _ in num_of_hand_shakes:            
    #     print(_)
    return len(num_of_hand_shakes)

# printHandshakes(['Alice', 'Bob', 'Carol', 'David'])

assert printHandshakes(['Alice', 'Bob']) == 1
assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3
assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6
assert printHandshakes(['Alice', 'Bob', 'Carol', 'David', "Rick"]) == 10
print()
print("All tests passed.")
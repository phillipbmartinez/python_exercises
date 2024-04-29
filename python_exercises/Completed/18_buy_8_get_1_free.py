def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
    total_price = 0
    cups_till_free_cup = 8

    while cups_till_free_cup > 0:
        if numberOfCoffees > 0:
            numberOfCoffees -= 1
            total_price += pricePerCoffee
            cups_till_free_cup -= 1
        else:
            break

        if cups_till_free_cup == 0:
            numberOfCoffees -= 1
            cups_till_free_cup = 8
            

    return total_price

# print(getCostOfCoffee(7, 2.50))
# print(getCostOfCoffee(8, 2.50))
# print(getCostOfCoffee(9, 2.50))
# print(getCostOfCoffee(10, 2.50))


assert getCostOfCoffee(7, 2.50) == 17.50
assert getCostOfCoffee(8, 2.50) == 20
assert getCostOfCoffee(9, 2.50) == 20
assert getCostOfCoffee(10, 2.50) == 22.50
for i in range(1, 4):
    assert getCostOfCoffee(0, i) == 0
    assert getCostOfCoffee(8, i) == 8 * i
    assert getCostOfCoffee(9, i) == 8 * i
    assert getCostOfCoffee(18, i) == 16 * i
    assert getCostOfCoffee(19, i) == 17 * i
    assert getCostOfCoffee(30, i) == 27 * i

print()
print("All assert statements passed successfully.")


# Another way to solve this problem
# def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
#     # Track the total price:
#     totalPrice = 0
#     # Track how many coffees we have until we get a free one:
#     cupsUntilFreeCoffee = 8

#     # Loop until the number of coffees to buy reaches 0:
#     while numberOfCoffees > 0:
#         # Decrement the number of coffees left to buy:
#         numberOfCoffees -= 1

#         # If this cup of coffee is free, reset the number to buy until
#         # a free cup back to 8:
#         if cupsUntilFreeCoffee == 0:
#             cupsUntilFreeCoffee = 8
#         # Otherwise, pay for a cup of coffee:
#         else:
#             # Increase the total price:
#             totalPrice += pricePerCoffee
#             # Decrement the coffees left until we get a free coffee:
#             cupsUntilFreeCoffee -= 1

#     # Return the total price:
#     return totalPrice


# Another way
# Create a getCostOfCoffee() function with parameters named numberOfCoffees and pricePerCoffee:
# def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
#     # Calculate the number of free coffees we get in this order:
#     numberOfFreeCoffees = numberOfCoffees // 9

#     # Calculate the number of coffees we will have to pay for in this order:
#     numberOfPaidCoffees = numberOfCoffees - numberOfFreeCoffees

#     # Calculate and return the price:
#     return numberOfPaidCoffees * pricePerCoffee
#     #return (numberOfCoffees - (numberOfCoffees // 9)) * pricePerCoffee
import math

def convertToFahrenheit(degreesCelsius):
    fahrenheit = round(degreesCelsius * (9/5) + 32, 2)
    print(fahrenheit)

def convertToCelsius(degreesFarenheit):
    celsius = round((degreesFarenheit - 32) * (5/9), 2)
    print(celsius)

convertToCelsius(0)
convertToCelsius(180)
convertToFahrenheit(0)
convertToFahrenheit(100)
#convertToCelsius(convertToFahrenheit(15))

"""def convertToFahrenheit(degreesCelsius):
    # Calculate and return the degrees Fahrenheit:
    return degreesCelsius * (9 / 5) + 32


def convertToCelsius(degreesFahrenheit):
    # Calculate and return the degrees Celsius:
    return (degreesFahrenheit - 32) * (5 / 9)

assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15"""
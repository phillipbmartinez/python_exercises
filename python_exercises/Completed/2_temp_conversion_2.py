def convertToFahrenheit(degressCelsius):
    degreesFahrenheit = degressCelsius * (9/5) + 32
    return degreesFahrenheit

def convertToCelsius(degreesFahrenheit):
    degreesCelsius = (degreesFahrenheit - 32) * (5/9)
    return degreesCelsius

assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15
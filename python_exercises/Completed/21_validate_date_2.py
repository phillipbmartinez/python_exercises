def isLeapYear(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False
    
def isValidDate(year, month, day):
    month_30_days = [4, 6, 9, 11]
    month_31_days = [1, 3, 5, 7, 8, 10, 12]
    
    if (month < 1 or month > 12):
        return False
    
    if (day < 1 or day > 31):
        return False
    
    if isLeapYear(year) == False and (month > 0 and month <= 12):
        if month == 2 and day == 29:
            return False
        elif month != 2 and day == 29:
            return True
        elif month in month_30_days and day > 30:
            return False
        elif month in month_31_days and day > 31:
            return False
        else:
            return True

    if isLeapYear(year) == True and (month > 0 and month <= 12):
        if month == 2 and (day > 0 or day < 30):
            return True
        elif month != 2 and day == 29:
            return True
        elif month in month_30_days and day > 30:
            return False
        elif month in month_31_days and day > 31:
            return False
        else:
            return True

    
assert isLeapYear(1999) == False
assert isLeapYear(2000) == True
assert isLeapYear(2001) == False
assert isLeapYear(2004) == True
assert isLeapYear(2100) == False
assert isLeapYear(2400) == True
assert isLeapYear(1000000) == True
print("All tests passed.")
print()
    
assert isValidDate(1999, 12, 31) == True
assert isValidDate(2000, 2, 29) == True
assert isValidDate(2001, 2, 29) == False
assert isValidDate(2029, 13, 1) == False
assert isValidDate(1000000, 1, 1) == True
assert isValidDate(2015, 4, 31) == False
assert isValidDate(1970, 5, 99) == False
assert isValidDate(1981, 0, 3) == False
assert isValidDate(1666, 4, 0) == False
print("All initial tests passed.")

import datetime
d = datetime.date(1970, 1, 1)
oneDay = datetime.timedelta(days=1)
for i in range(1000000):
    assert isValidDate(d.year, d.month, d.day) == True
    d += oneDay
print("Final loop tests passed.")
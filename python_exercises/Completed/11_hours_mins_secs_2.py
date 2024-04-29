def getHoursMinutesSeconds(totalSeconds):
    if totalSeconds == 0:
        return "0s"
    
    hours = 0
    minutes = 0
    seconds = 0
    total_time = []

    while totalSeconds >= 3600:
        totalSeconds -= 3600
        hours += 1
    
    if hours == 0:
        pass
    else:
        total_time.append(str(hours) + "h")

    if totalSeconds >= 60:
        totalSeconds -= 60
        minutes += 1
        total_time.append(str(minutes) + "m")

    if totalSeconds < 60 and totalSeconds != 0:
        seconds = totalSeconds
        total_time.append(str(seconds) + "s")

    # print(" ".join(total_time))
    return " ".join(total_time)
    
# getHoursMinutesSeconds(30)
# getHoursMinutesSeconds(60)
# getHoursMinutesSeconds(90)
# getHoursMinutesSeconds(3600)
# getHoursMinutesSeconds(3601)
# getHoursMinutesSeconds(90042)
# getHoursMinutesSeconds(0)

assert getHoursMinutesSeconds(30) == '30s'
assert getHoursMinutesSeconds(60) == '1m'
assert getHoursMinutesSeconds(90) == '1m 30s'
assert getHoursMinutesSeconds(3600) == '1h'
assert getHoursMinutesSeconds(3601) == '1h 1s'
assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
assert getHoursMinutesSeconds(0) == '0s'
assert getHoursMinutesSeconds(90042) == '25h 42s'

print()
print("All assert statements passed!")
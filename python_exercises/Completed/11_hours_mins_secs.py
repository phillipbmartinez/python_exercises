def getHoursMinutesSeconds(totalSeconds):
    if totalSeconds == 0:
        return "0s"
    
    hours = 0
    while totalSeconds >= 3600:
        hours += 1
        totalSeconds -= 3600
    
    minutes = 0
    while totalSeconds >= 60:
        minutes += 1
        totalSeconds -= 60
    
    seconds = totalSeconds

    time_list = []
    if hours > 0:
        time_list.append(str(hours) + "h")
    if minutes > 0:
        time_list.append(str(minutes) + "m")
    if seconds > 0:
        time_list.append(str(seconds) + "s")
    #print(" ".join(time_list)) 
    return " ".join(time_list)

# getHoursMinutesSeconds(30)
# getHoursMinutesSeconds(60)
# getHoursMinutesSeconds(90)
# getHoursMinutesSeconds(3600)
# getHoursMinutesSeconds(3601)
# getHoursMinutesSeconds(3661)
# getHoursMinutesSeconds(90042)
# getHoursMinutesSeconds(0)

assert getHoursMinutesSeconds(30) == '30s'
assert getHoursMinutesSeconds(60) == '1m'
assert getHoursMinutesSeconds(90) == '1m 30s'
assert getHoursMinutesSeconds(3600) == '1h'
assert getHoursMinutesSeconds(3601) == '1h 1s'
assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
assert getHoursMinutesSeconds(90042) == '25h 42s'
assert getHoursMinutesSeconds(0) == '0s'
print("All tests passed.")

##################################################################################
def getHoursMinutesSeconds(totalSeconds):
    # If totalSeconds is 0, just return '0s':
    if totalSeconds == 0:
        return "0s"
    # Set hours to how many times 3600 seconds can divide
    # totalSeconds. Then set totalSeconds to the remainder:
    if totalSeconds >= 3600:
        hours = totalSeconds // 3600
        totalSeconds = totalSeconds % 3600
    else:
        hours = 0
    # Set minutes to how many times 60 seconds can divide
    # totalSeconds. Then set totalSeconds to the remainder:
    if totalSeconds >= 60:
        minutes = totalSeconds // 60
        totalSeconds = totalSeconds % 60
    else:
        minutes = 0
    # Set seconds to the remaining totalSeconds value:
    seconds = totalSeconds
    # Create an hms list that contains the string hour/minute/second amounts:
    hms = []
    # If there are one or more hours, add the amount with an 'h' suffix:
    if hours > 0:
        hms.append(str(hours) + 'h')
    # If there are one or more minutes, add the amount with an 'm' suffix:
    if minutes > 0:
        hms.append(str(minutes) + 'm')
    # If there are one or more seconds, add the amount with an 's' suffix:
    if seconds > 0:
        hms.append(str(seconds) + 's')
    # Join the hour/minute/second strings with a space in between them:
    return ' '.join(hms)
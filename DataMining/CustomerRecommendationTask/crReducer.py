import sys 
import re 

currentTravellerType = None
currentYesCount = None 
travellerType = None

for line in sys.stdin:
    line = line.strip()
    travellerType, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue

    if currentTravellerType == travellerType:
        currentYesCount += count
    else:
        if currentTravellerType:
            print ('%s\t%s' % (currentTravellerType, currentYesCount))
        currentYesCount = count
        currentTravellerType = travellerType

if currentTravellerType == travellerType:
    print('%s\t%s' % (currentTravellerType, currentYesCount))
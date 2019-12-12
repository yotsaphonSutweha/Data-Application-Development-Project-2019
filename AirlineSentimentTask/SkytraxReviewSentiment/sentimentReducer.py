import sys 

overallPositve = 0
overallNegative = 0
overallNeutral = 0
for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    line = line.split("\t")
    sentiment = line[1]
    if sentiment == "positive":
        overallPositve = overallPositve + 1
    elif sentiment == "negative":
        overallNegative = overallNegative + 1
    else:
        overallNeutral = overallNeutral + 1

print('%s\t%s' % ("Positive", overallPositve))
print('%s\t%s' % ("Negative", overallNegative))
print('%s\t%s' % ("Neutral", overallNeutral))
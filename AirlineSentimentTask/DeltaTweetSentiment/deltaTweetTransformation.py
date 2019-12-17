import sys 
numPositive = 0
numNegative = 0
numNeutral = 0
# Data transformation: counting how many positive, negative and neutral sentiment are present within the dataset in order to determine how the informal public opinion from Twitter affects Delta airline
for line in sys.stdin:
    line = line.strip()
    if line == "positive":
        numPositive = numPositive + 1
    elif line =="negative":
        numNegative = numNegative + 1
    else:
        numNeutral = numNeutral + 1
        
print('%s\t%s' % ("Sentiment", "Count"))
print("%s\t%s" % ("Positive", numPositive))
print("%s\t%s" % ("Negative", numNegative))
print("%s\t%s" % ("Neutral", numNeutral))
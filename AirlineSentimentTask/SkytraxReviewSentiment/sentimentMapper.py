import sys 
import re 

def readWords(filename):
    words = []
    with open(filename, encoding="ISO-8859-1") as f:
        for line in f:
            if line.startswith(';') or line.strip()=='':
                continue
            words.append(line.strip())
    return words

positiveWords = readWords("./AirlineSentimentTask/SkytraxReviewSentiment/dictionaries/hu-liu-positive-words.txt")
negativeWords = readWords("./AirlineSentimentTask/SkytraxReviewSentiment/dictionaries/hu-liu-negative-words.txt")

commentNum = 0
for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    words = line.split()
    positiveCounts = 0
    negativeCounts = 0
    sentimentResult = ""
    for word in words:
        if word in positiveWords:
            positiveCounts = positiveCounts + 1
        elif word in negativeWords:
            negativeCounts = negativeCounts + 1
    if positiveCounts > negativeCounts:
        sentimentResult = "Positive"
    elif positiveCounts < negativeCounts:
        sentimentResult = "Negative"
    else:
        sentimentResult = "Neutral"
    commentNum = commentNum + 1
    print('%s\t%s' % (commentNum, sentimentResult))
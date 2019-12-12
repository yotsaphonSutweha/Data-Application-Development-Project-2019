import pandas as pd 

skytraxSentimentResults = []
tweetSentimentResults = []
skytraxSentimenDataPath = '../SkytraxReviewSentiment/output/skyTrax2015SentimentReducerOutputs.txt'
deltaTweetSentimentPath = '../DeltaTweetSentiment/Output/deltaTweetTransformationOutput.txt'

df1 = pd.read_csv(skytraxSentimenDataPath, delimiter="\t")
for line in df1:
    line = line.strip()
    # get only number

table = {
    'Sentiment Score': ['Positive', 'Negative', 'Neutral'],
    'Skytrax Sentiment': [],
    'Tweet Sentiment': []
}


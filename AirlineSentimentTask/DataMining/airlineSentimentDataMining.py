import pandas as pd 

skytraxSentimentResults = []
tweetSentimentResults = []
skytraxSentimenDataPath = '../SkytraxReviewSentiment/output/skyTrax2015SentimentReducerOutputs.txt'
deltaTweetSentimentPath = '../DeltaTweetSentiment/Output/deltaTweetTransformationOutput.txt'

df1 = pd.read_csv(skytraxSentimenDataPath, delimiter="\t")
skytraxPositive = df1['Count'][0]
skytraxNegative = df1['Count'][1]
skytraxNeutral = df1['Count'][2]
df2 = pd.read_csv(deltaTweetSentimentPath, delimiter="\t")
deltaTweetPositive = df2['Count'][0]
deltaTweetNegative = df2['Count'][1]
deltaTweetNeutral = df2['Count'][2]


table = {
    'Sentiment': ['Positive', 'Negative', 'Neutral'],
    'Skytrax sentiment score': [skytraxPositive, skytraxNegative, skytraxNeutral],
    'Tweet sentiment score': [deltaTweetPositive, deltaTweetNegative, deltaTweetNeutral ]
}


dataframe = pd.DataFrame(table, columns=['Sentiment', 'Skytrax sentiment score', 'Tweet sentiment score'])

dataframe.to_csv(r'./Output/sentiment_analysis_table_results.csv', index=None, header=True)


import pandas as pd 
dataset = pd.read_csv("./Airline-Sentiment-2-w-AA_DELTA.csv")

# Data selection process: taking only airline sentiment column from the entire dataset for transformation
airlineSentiment = dataset['airline_sentiment']
for sentiment in airlineSentiment:
    print(sentiment)
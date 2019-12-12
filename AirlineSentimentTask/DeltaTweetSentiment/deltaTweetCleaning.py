import pandas as pd 
dataset = pd.read_csv("../../Airline-Sentiment-2-w-AA_DELTA.csv")
print("Dataset instances: {0}".format(len(dataset)))
airlineSentiment = dataset['airline_sentiment']
print("Airline sentiment column instances: {0}".format(len(airlineSentiment)))
print("Airline sentiment column head:")
print(airlineSentiment.head())
print("---------Airline sentiment description---------")
print(airlineSentiment.describe())
print("-----------------------------------------------")

print("As part of data pre-processing, airline sentiment tweet went through data cleaning process, as the result no missing values are present as the number of instances of the dataset matches the number of intances of the airline_sentitment column, also the type of the attribute for each intance is the same. To conclude, there is no need for additional cleaning process")
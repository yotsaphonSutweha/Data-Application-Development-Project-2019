import pandas as pd 
import matplotlib as plt

# ---- 2015 ------
df2015 = pd.read_csv("./skytrax_reviews_delta_2015_cleaning.csv")
print("-----------------Skytrax 2015 dataset-------------------")
print(df2015.head(5))
print(df2015.describe())
catAttr2015 = df2015[["review_title", "publish_date", "reviewer_name", "review_comment", "aircraft",   "traveller_type", "seat_type", "route", "date_flown", "recommend"]].copy()
print(catAttr2015.describe())
print("---------------------------------------------------------\n")
#--------------------

# -----2019 - 2016 Dataset -------
skytrax = pd.read_csv("./skytrax_2019-2016_dataset.csv")
print("-----------------Skytrax 2019 - 2016 dataset-------------------")
print(skytrax.head(5))
print(skytrax.describe())
catAttrSytrax = skytrax[["review_title", "publish_date", "reviewer_name", "review_comment", "aircraft",   "traveller_type", "seat_type", "route", "date_flown", "recommend"]].copy()
print(catAttrSytrax.describe())
print("---------------------------------------------------------\n")
#--------------------

# -----Delta Feb 2015-------
dfDeltaSentiment2015 = pd.read_csv("./Airline-Sentiment-2-w-AA_DELTA.csv")
print("----------------Delta airline sentiment 2015 dataset-------------------")
print(dfDeltaSentiment2015.head(5))
print(dfDeltaSentiment2015.describe())
catDeltaSntiment2015 = dfDeltaSentiment2015[["airline_sentiment", "negativereason", "name", "tweet_location", "user_timezone"]].copy()
print(catDeltaSntiment2015.describe())
print("---------------------------------------------------------\n")
#--------------------




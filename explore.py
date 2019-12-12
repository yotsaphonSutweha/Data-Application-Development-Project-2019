import pandas as pd 
import numpy as np
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


# print(df.head(10))

# print(df.describe())

# Delete irrelavant columns: title, comment, aircraft, date flown
# newdf = df2016.drop(columns=["review_title", "review_comment", "aircraft", "date_flown"])
# There columns are not relavant becuase the title and comment are not suitable for the trend analysis. The aircraft section do not tell much about the public opinion. 

# print(newdf.head(10))
# Describe numeric attributes
# numAttr = newdf[["overall_rating", "seat_comfort_rating", "cabin_service_rating", "food_and_beverages_rating", "inflight_entertainment_rating", "ground_service_rating", "wifi_connectivity_rating", "value_for_money_rating"]].copy()

# # Describe categorical attributes
# catAttr = newdf[["publish_date", "traveller_type", "seat_type", "route", "recommend"]].copy()

# Now we know that there are no missing values from the dataset, we also gain an insight on the characteristics of the numeric attr of the dataset
# print(numAttr.describe())

# # We look into the categorical data from the datset and have the insights on the most popular seat_type, traveller_type and the most frequent date that the customers make the reviews. Also we can see that the customers do not recommend the airline with 111 customers saying no, out of 218.
# print(catAttr.describe())

# print(numAttr.groupby('seat_comfort_rating').size())
# print(numAttr.groupby('cabin_service_rating').size())
# print(numAttr.groupby('food_and_beverages_rating').size()) # Have missing values
# print(numAttr.groupby('inflight_entertainment_rating').size()) # Have missing values
# print(numAttr.groupby('ground_service_rating').size())
# print(numAttr.groupby('wifi_connectivity_rating').size()) # Have missing values
# print(numAttr.groupby('value_for_money_rating').size())

# fillna()
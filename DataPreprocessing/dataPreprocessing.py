import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
data = pd.read_csv('./Skytrax_2016-2019_data_selection/Output/skytrax_2016-2019_data_selected_dataset.csv')

catData = data[['publish_date', 'traveller_type', 'recommend']].copy()

# No missing values for categorical, date data
print(catData.describe())
print(data.head())
# According to this, the data doesn't have any missing values however the ratings contain a lot of zero values which indicates that the values are missing as they were not being typed in by the customer. Theses values have to be dealt with.
print(data.describe())
# cabin_service_rating  food_and_beverages_rating  inflight_entertainment_rating  ground_service_rating  wifi_connectivity_rating  value_for_money_rating

# Check for missing values
overallRatingMissingValues = data[data['overall_rating'] == 0]
seatComfortRatingMissingValues = data[data['seat_comfort_rating'] == 0]
cabinServiceRatingMissingValues = data[data['cabin_service_rating'] == 0]
foodAndBeveragesRatingMissingValues = data[data['food_and_beverages_rating'] == 0]
inflightEntertainmentRatingMissingValues = data[data['inflight_entertainment_rating'] == 0]
groundServiceRatingMissingValues = data[data['ground_service_rating'] == 0]
wifiRatingMissingValues = data[data['wifi_connectivity_rating'] == 0]
valueForMoneyMissingValues = data[data['value_for_money_rating'] == 0]

print('Overall rating missing values : {0}'.format(len(overallRatingMissingValues))) # No need 
print('Seat comfort rating missing values: {0}'.format(len(seatComfortRatingMissingValues)))
print('Cabin service rating missing values: {0}'.format(len(cabinServiceRatingMissingValues)))
print('Food and beverages rating missing values: {0}'.format(len(foodAndBeveragesRatingMissingValues)))
print('Inflight entertainment rating missing values: {0}'.format(len(inflightEntertainmentRatingMissingValues)))
print('Ground service rating missig values: {0}'.format(len(groundServiceRatingMissingValues)))
print("Wifi connectivity rating missing values: {0}".format(len(wifiRatingMissingValues)))
print("Value for money rating missing values: {0}".format(len(valueForMoneyMissingValues))) # No need

# Check for outliers 
boxplot1 = sns.boxplot(y=data['overall_rating'])
fig1 = boxplot1.get_figure()
fig1.savefig("./DataPreprocessing/Output/Boxplots/check_outlier_boxploat1.png")
boxplot1.get_figure().clf()
boxplot2 = sns.boxplot(y=data['seat_comfort_rating'])
fig2 = boxplot2.get_figure()
fig2.savefig("./DataPreprocessing/Output/Boxplots/check_outlier_boxploat2.png")
boxplot2.get_figure().clf()
boxplot3 = sns.boxplot(y=data['cabin_service_rating'])
fig3 = boxplot3.get_figure()
fig3.savefig("./DataPreprocessing/Output/Boxplots/check_outlier_boxploat3.png")
boxplot3.get_figure().clf()
boxplot4 = sns.boxplot(y=data['food_and_beverages_rating'])
fig4 = boxplot4.get_figure()
fig4.savefig("./DataPreprocessing/Output/Boxplots/check_outlier_boxploat4.png")
boxplot4.get_figure().clf()
boxplot5 = sns.boxplot(y=data['inflight_entertainment_rating'])
fig5 = boxplot5.get_figure()
fig5.savefig("./DataPreprocessing/Output/Boxplots/check_outlier_boxploat5.png")
boxplot5.get_figure().clf()
boxplot6 = sns.boxplot(y=data['ground_service_rating'])
fig6 = boxplot6.get_figure()
fig6.savefig("./DataPreprocessing/Output/Boxplots/check_outlier_boxploat6.png")
boxplot6.get_figure().clf()
boxplot7 = sns.boxplot(y=data['wifi_connectivity_rating'])
fig7 = boxplot7.get_figure()
fig7.savefig("./DataPreprocessing/Output/Boxplots/check_outlier_boxploat7.png")
boxplot7.get_figure().clf()
boxplot8= sns.boxplot(y=data['value_for_money_rating'])
fig8 = boxplot8.get_figure()
fig8.savefig("./DataPreprocessing/Output/Boxplots/check_outlier_boxploat8.png")
boxplot8.get_figure().clf()
# No outliers are present in the numerical values

# Dealing with missing values

seatComfortRatings = data[data['seat_comfort_rating'] != 0]
print(seatComfortRatings['seat_comfort_rating'].median())
seatComfortRatingsMedian = seatComfortRatings['seat_comfort_rating'].median()
data['seat_comfort_rating'].replace(0, seatComfortRatingsMedian, inplace=True)
print(len(data[data['seat_comfort_rating'] == 0]))

# Cabin service 
cabinServiceRatings = data[data['cabin_service_rating'] != 0]
print(cabinServiceRatings['cabin_service_rating'].median())
cabinServiceRatingsMedian = cabinServiceRatings['cabin_service_rating'].median()
data['cabin_service_rating'].replace(0, cabinServiceRatingsMedian, inplace=True)
print(len(data[data['cabin_service_rating'] == 0]))

# Food and beverages  
foodAndBeveragesRatings = data[data['food_and_beverages_rating'] != 0]
foodAndBeveragesRatingsMedian = foodAndBeveragesRatings['food_and_beverages_rating'].median()
data['food_and_beverages_rating'].replace(0, foodAndBeveragesRatingsMedian, inplace = True)
# inflight entertainment
inflightEntertainmentRatings = data[data['inflight_entertainment_rating'] != 0]
inflightEntertainmentRatingsMedian = inflightEntertainmentRatings['inflight_entertainment_rating'].median()
data['inflight_entertainment_rating'].replace(0, inflightEntertainmentRatingsMedian, inplace=True)
# Ground service 
groundServiceRatings = data[data['ground_service_rating'] != 0]
groundServiceRatingsMedian = groundServiceRatings['ground_service_rating'].median()
data['ground_service_rating'].replace(0, groundServiceRatingsMedian, inplace=True)
# Wifi connectivity 
wifiConnectivityRatings = data[data['wifi_connectivity_rating']!=0]
wifiConnectivityRatingsMedian = wifiConnectivityRatings['wifi_connectivity_rating'].median()
data['wifi_connectivity_rating'].replace(0, wifiConnectivityRatingsMedian, inplace=True)


# Ensure that there are no zero values appearing in the dataset
overallRatingMissingValues = data[data['overall_rating'] == 0]
seatComfortRatingMissingValues = data[data['seat_comfort_rating'] == 0]
cabinServiceRatingMissingValues = data[data['cabin_service_rating'] == 0]
foodAndBeveragesRatingMissingValues = data[data['food_and_beverages_rating'] == 0]
inflightEntertainmentRatingMissingValues = data[data['inflight_entertainment_rating'] == 0]
groundServiceRatingMissingValues = data[data['ground_service_rating'] == 0]
wifiRatingMissingValues = data[data['wifi_connectivity_rating'] == 0]
valueForMoneyMissingValues = data[data['value_for_money_rating'] == 0]

print('Seat comfort rating missing values: {0}'.format(len(seatComfortRatingMissingValues)))
print('Cabin service rating missing values: {0}'.format(len(cabinServiceRatingMissingValues)))
print('Food and beverages rating missing values: {0}'.format(len(foodAndBeveragesRatingMissingValues)))
print('Inflight entertainment rating missing values: {0}'.format(len(inflightEntertainmentRatingMissingValues)))
print('Ground service rating missig values: {0}'.format(len(groundServiceRatingMissingValues)))
print("Wifi connectivity rating missing values: {0}".format(len(wifiRatingMissingValues)))

data.to_csv(r'./DataPreprocessing/Output/pre_processed_skytrax_dataset.csv', index=None, header=True)
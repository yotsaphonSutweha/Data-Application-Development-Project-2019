import pandas as pd 
data = pd.read_csv('./DataPreprocessing/Output/pre_processed_skytrax_dataset.csv')

seatComfortRatingMean = round(data['seat_comfort_rating'].mean(), 2)
cabinServiceRatingMean = round(data['cabin_service_rating'].mean(), 2)
foodAndBeveragesRatingMean = round(data['food_and_beverages_rating'].mean(), 2)
inflightEntertainmentRatingMean = round(data['inflight_entertainment_rating'].mean(), 2)
groundServiceRatingMean = round(data['ground_service_rating'].mean())
wifiConnectivityRatingMean = round(data['wifi_connectivity_rating'].mean())

officialRatingsAnalysis = {
    'Leisure rating' : ['Seat comfort rating', 'Cabin service rating', 'Food and beverages rating', 'Inflight entertainment rating', 'Ground service rating', 'Wifi connectivity rating'],
    'Mean value' : [seatComfortRatingMean, cabinServiceRatingMean, foodAndBeveragesRatingMean, inflightEntertainmentRatingMean, groundServiceRatingMean, wifiConnectivityRatingMean]
}

dataframe = pd.DataFrame(officialRatingsAnalysis, columns=['Leisure rating', 'Mean value'])

dataframe.to_csv(r'./DataTransformation/AirlineLeisureRatingsTask/Output/leisure_rating_analysis.csv', index=None, header=True)
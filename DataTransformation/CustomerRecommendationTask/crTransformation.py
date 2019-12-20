# The second data selection process
import pandas as pd 
data = pd.read_csv('./DataPreprocessing/Output/pre_processed_skytrax_dataset.csv')
data.drop('publish_date', axis=1, inplace=True)
data.drop('overall_rating', axis=1, inplace=True)
data.drop('seat_comfort_rating', axis=1, inplace=True)
data.drop('cabin_service_rating', axis=1, inplace=True)
data.drop('food_and_beverages_rating', axis=1, inplace=True)
data.drop('inflight_entertainment_rating', axis=1, inplace=True)
data.drop('ground_service_rating', axis=1, inplace=True)
data.drop('wifi_connectivity_rating', axis=1, inplace=True)
data.drop('value_for_money_rating', axis=1, inplace=True)
data.to_csv(r'./DataTransformation/CustomerRecommendationTask/Output/customer_recommendation_analysis.txt', index=None, header=False, sep=' ')
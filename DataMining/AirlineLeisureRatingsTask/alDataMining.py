import pandas as pd 
import seaborn as sns
from matplotlib import pyplot as plt

officialRatingAnalysisData = pd.read_csv('./DataTransformation/AirlineLeisureRatingsTask/Output/leisure_rating_analysis.csv')

chart = sns.catplot(x='Leisure rating', y='Mean value', kind='bar', data=officialRatingAnalysisData)
chart.set(ylim=(0, 5))
chart.set_xticklabels(horizontalalignment='right', fontsize='small', rotation=70)
chart.savefig("./DataMining/AirlineLeisureRatingsTask/Output/airline_leisure_ratings.png")



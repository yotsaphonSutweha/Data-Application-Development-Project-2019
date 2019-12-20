import pandas as pd 
import seaborn as sns
from matplotlib import pyplot as plt

overallRatingAnalysisData = pd.read_csv('./DataTransformation/OverallRatingTask/Output/overall_rating_analysis_dataset.csv')

chart = sns.catplot(x='Month', y='Overall Rating Mean', kind='bar', palette='Set1', data=overallRatingAnalysisData)
chart.set_xticklabels(horizontalalignment='right', fontsize='small', rotation=70)
chart.savefig("./DataMining/OverallRatingTask/Output/Customer_overall_rating_trend.png")


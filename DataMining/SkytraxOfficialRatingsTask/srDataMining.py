import pandas as pd 
import seaborn as sns
from matplotlib import pyplot as plt

officialRatingAnalysisData = pd.read_csv('../../DataTransformation/SkytraxOfficialRatingsTask/Output/official_rating_analysis.csv')

chart = sns.catplot(x='Skytrax official rating', y='Mean value', kind='bar', data=officialRatingAnalysisData)
chart.set(ylim=(0, 5))
chart.set_xticklabels(horizontalalignment='right', fontsize='small', rotation=70)
plt.show()
chart.savefig("./Output/Delta_airline_provisional_customer_satisfaction.png")

data = pd.read_csv('../../DataPreprocessing/Output/pre_processed_skytrax_dataset.csv')

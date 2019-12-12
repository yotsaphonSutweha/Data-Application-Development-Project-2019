import pandas as pd 
import seaborn as sns
from matplotlib import pyplot as plt
data = pd.read_csv('../../DataPreprocessing/Output/pre_processed_skytrax_dataset.csv')

#-----------------2019-------------------
nov2019 = data[data['publish_date'].str.contains('2019-11')]
oct2019 = data[data['publish_date'].str.contains('2019-10')]
sept2019 = data[data['publish_date'].str.contains('2019-09')]
aug2019 = data[data['publish_date'].str.contains('2019-08')]
july2019 = data[data['publish_date'].str.contains('2019-07')]
june2019 = data[data['publish_date'].str.contains('2019-06')]
may2019 = data[data['publish_date'].str.contains('2019-05')]
apr2019 = data[data['publish_date'].str.contains('2019-04')]
march2019 = data[data['publish_date'].str.contains('2019-03')]
feb2019 = data[data['publish_date'].str.contains('2019-02')]
jan2019 = data[data['publish_date'].str.contains('2019-01')]
nov2019Mean = round(nov2019['overall_rating'].mean())
oct2019Mean = round(oct2019['overall_rating'].mean())
sept2019Mean = round(sept2019['overall_rating'].mean())
aug2019Mean = round(aug2019['overall_rating'].mean())
july2019Mean = round(july2019['overall_rating'].mean())
june2019Mean = round(june2019['overall_rating'].mean())
may2019Mean = round(may2019['overall_rating'].mean())
apr2019Mean = round(apr2019['overall_rating'].mean())
march2019Mean = round(march2019['overall_rating'].mean())
feb2019Mean = round(feb2019['overall_rating'].mean())
jan2019Mean = round(jan2019['overall_rating'].mean())
#----------------------------------------


#-----------------2018-------------------
dec2018 = data[data['publish_date'].str.contains('2018-12')]
nov2018 = data[data['publish_date'].str.contains('2018-11')]
oct2018 = data[data['publish_date'].str.contains('2018-10')]
sept2018 = data[data['publish_date'].str.contains('2018-09')]
aug2018 = data[data['publish_date'].str.contains('2018-08')]
july2018 = data[data['publish_date'].str.contains('2018-07')]
june2018 = data[data['publish_date'].str.contains('2018-06')]
may2018 = data[data['publish_date'].str.contains('2018-05')]
apr2018 = data[data['publish_date'].str.contains('2018-04')]
march2018 = data[data['publish_date'].str.contains('2018-03')]
feb2018 = data[data['publish_date'].str.contains('2018-02')]
jan2018 = data[data['publish_date'].str.contains('2018-01')]
dec2018Mean = round(dec2018['overall_rating'].mean())
nov2018Mean = round(nov2018['overall_rating'].mean())
oct2018Mean = round(oct2018['overall_rating'].mean())
sept2018Mean = round(sept2018['overall_rating'].mean())
aug2018Mean = round(aug2018['overall_rating'].mean())
july2018Mean = round(july2018['overall_rating'].mean())
june2018Mean = round(june2018['overall_rating'].mean())
may2018Mean = round(may2018['overall_rating'].mean())
apr2018Mean = round(apr2018['overall_rating'].mean())
march2018Mean = round(march2018['overall_rating'].mean())
feb2018Mean = round(feb2018['overall_rating'].mean())
jan2018Mean = round(jan2018['overall_rating'].mean())
#----------------------------------------


#-----------------2017-------------------
dec2017 = data[data['publish_date'].str.contains('2017-12')]
nov2017 = data[data['publish_date'].str.contains('2017-11')]
oct2017 = data[data['publish_date'].str.contains('2017-10')]
sept2017 = data[data['publish_date'].str.contains('2017-09')]
aug2017 = data[data['publish_date'].str.contains('2017-08')]
july2017 = data[data['publish_date'].str.contains('2017-07')]
june2017 = data[data['publish_date'].str.contains('2017-06')]
may2017 = data[data['publish_date'].str.contains('2017-05')]
apr2017 = data[data['publish_date'].str.contains('2017-04')]
march2017 = data[data['publish_date'].str.contains('2017-03')]
feb2017 = data[data['publish_date'].str.contains('2017-02')]
jan2017 = data[data['publish_date'].str.contains('2017-01')]
dec2017Mean = round(dec2017['overall_rating'].mean())
nov2017Mean = round(nov2017['overall_rating'].mean())
oct2017Mean = round(oct2017['overall_rating'].mean())
sept2017Mean = round(sept2017['overall_rating'].mean())
aug2017Mean = round(aug2017['overall_rating'].mean())
july2017Mean = round(july2017['overall_rating'].mean())
june2017Mean = round(june2017['overall_rating'].mean())
may2017Mean = round(may2017['overall_rating'].mean())
apr2017Mean = round(apr2017['overall_rating'].mean())
march2017Mean = round(march2017['overall_rating'].mean())
feb2017Mean = round(feb2017['overall_rating'].mean())
jan2017Mean = round(jan2017['overall_rating'].mean())
#----------------------------------------


#-----------------2016-------------------
dec2016 = data[data['publish_date'].str.contains('2016-12')]
nov2016 = data[data['publish_date'].str.contains('2016-11')]
dec2016Mean = round(dec2016['overall_rating'].mean())
nov2016Mean = round(nov2016['overall_rating'].mean())
#----------------------------------------

OverallRatingAnalysis = {
    'Month' : ['Nov 2016', 'Dec 2016', 'Jan 2017', 'Feb 2017', 'March 2017','Apr 2017','May 2017','June 2017','July 2017','Aug 2017','Sept 2017','Oct 2017','Nov 2017','Dec 2017','Jan 2018','Feb 2018','March 2018','Apr 2018','May 2018','June 2018','July 2018','Aug 2018','Sept 2018','Oct 2018','Nov 2018','Dec 2018','Jan 2019','Feb 2019','March 2019','Apr 2019','May 2019','June 2019','July 2019','Aug 2019','Sept 2019','Oct 2019','Nov 2019',],
    'Overall Rating Mean': [nov2016Mean, dec2016Mean, jan2017Mean, feb2017Mean, march2017Mean, apr2017Mean, may2017Mean, june2017Mean, july2017Mean, aug2017Mean, sept2017Mean, oct2017Mean, nov2017Mean, dec2017Mean, jan2018Mean, feb2018Mean, march2018Mean, apr2018Mean, may2018Mean, june2018Mean, july2018Mean, aug2018Mean, sept2018Mean, oct2018Mean, nov2018Mean, dec2018Mean, jan2019Mean, feb2019Mean, march2019Mean, apr2019Mean, may2019Mean, june2019Mean, july2019Mean, aug2019Mean, sept2019Mean, oct2019Mean, nov2019Mean]
}

dataframe = pd.DataFrame(OverallRatingAnalysis, columns=['Month', 'Overall Rating Mean'])

dataframe.to_csv(r'./Output/overall_rating_analysis_dataset.csv', index=None, header=True)

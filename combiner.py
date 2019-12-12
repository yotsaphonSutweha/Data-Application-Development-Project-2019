import pandas as pd 
import glob 
skytrax = []

# This class is used to combine skytrax data from November 2019 - November 2016 after scrapped from the website
df1 = pd.read_csv("./SkytraxDataset/skytrax_reviews_delta_2019_cleaning.csv", index_col=None, header=0)
skytrax.append(df1)
df2 = pd.read_csv("./SkytraxDataset/skytrax_reviews_delta_2018_cleaning.csv", index_col=None, header=0)
skytrax.append(df2)
df3 = pd.read_csv("./SkytraxDataset/skytrax_reviews_delta_2017_cleaning.csv", index_col=None, header=0)
skytrax.append(df3)
df4 = pd.read_csv("./SkytraxDataset/skytrax_reviews_delta_2016_cleaning.csv", index_col=None, header=0)
skytrax.append(df4)

frame = pd.concat(skytrax, axis=0, ignore_index=True)
# Keep only the data from Nov 2019 - Nov 2016
jan = frame[frame['publish_date'].str.contains('2016-01')].index 
frame.drop(jan, inplace=True)
feb = frame[frame['publish_date'].str.contains('2016-02')].index 
frame.drop(feb, inplace=True)
mar = frame[frame['publish_date'].str.contains('2016-03')].index 
frame.drop(mar, inplace=True)
apr = frame[frame['publish_date'].str.contains('2016-04')].index 
frame.drop(apr, inplace=True)
may = frame[frame['publish_date'].str.contains('2016-05')].index 
frame.drop(may, inplace=True)
june = frame[frame['publish_date'].str.contains('2016-06')].index 
frame.drop(june, inplace=True)
july = frame[frame['publish_date'].str.contains('2016-07')].index 
frame.drop(july, inplace=True)
aug = frame[frame['publish_date'].str.contains('2016-08')].index 
frame.drop(aug, inplace=True)
sept = frame[frame['publish_date'].str.contains('2016-09')].index 
frame.drop(sept, inplace=True)
octo = frame[frame['publish_date'].str.contains('2016-10')].index 
frame.drop(octo, inplace=True)

frame.to_csv(r'./skytrax_2019-2016_dataset.csv', index=None, header=True)
   
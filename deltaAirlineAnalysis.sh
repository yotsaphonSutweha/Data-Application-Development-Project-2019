# Run combiner 
python combiner.py 

# Run data exploration 
python explore.py > exploratoryResults.txt

# ------------------Airline sentiment task---------------------------------
mkdir ./AirlineSentimentTask/SkytraxReviewSentiment/output
mkdir ./AirlineSentimentTask/DeltaTweetSentiment/Output
mkdir ./AirlineSentimentTask/DataMining/Output
# Skytrax 2015 text analysis using customer's comments
# Step 1: Pre-processing task for only getting the customer comments column
python ./AirlineSentimentTask/SkytraxReviewSentiment/skytrax2015Preprocessing.py > ./AirlineSentimentTask/SkytraxReviewSentiment/output/skyTrax2015PreprocessOutputs.txt

# Step 2: Using the Mapper to produce the results of sentiment score for each customer comment
cat ./AirlineSentimentTask/SkytraxReviewSentiment/output/skyTrax2015PreprocessOutputs.txt | python ./AirlineSentimentTask/SkytraxReviewSentiment/sentimentMapper.py > ./AirlineSentimentTask/SkytraxReviewSentiment/output/skyTrax2015SentimentMapperOutputs.txt

# Step 3: Using the Reducer to produce the overall sentiment scores for the Skytrax 2015 dataset 
cat ./AirlineSentimentTask/SkytraxReviewSentiment/output/skyTrax2015SentimentMapperOutputs.txt | python ./AirlineSentimentTask/SkytraxReviewSentiment/sentimentReducer.py > ./AirlineSentimentTask/SkytraxReviewSentiment/output/skyTrax2015SentimentReducerOutputs.txt 

# Delta tweet sentiment, find out the frequency of each sentiment score
# Step 4: Run Delta tweet cleaing
python ./AirlineSentimentTask/DeltaTweetSentiment/deltaTweetCleaning.py > ./AirlineSentimentTask/DeltaTweetSentiment/Output/deltaTweetCleaningOutput.txt

# Step 5: Run Delta tweet data selection 
python ./AirlineSentimentTask/DeltaTweetSentiment/deltaTweetDataSelection.py > ./AirlineSentimentTask/DeltaTweetSentiment/Output/deltaTweetDataSelectionOutput.txt

# Step 6: Run Delta tweet data transformation
cat ./AirlineSentimentTask/DeltaTweetSentiment/Output/deltaTweetDataSelectionOutput.txt | python ./AirlineSentimentTask/DeltaTweetSentiment/deltaTweetTransformation.py > ./AirlineSentimentTask/DeltaTweetSentiment/Output/deltaTweetTransformationOutput.txt

# Step 7: Run airline sentiment data mining 
python ./AirlineSentimentTask/DataMining/airlineSentimentDataMining.py

#-------------------------------------------------------------------------------

#---------------------Skytrax 2016 - 2019 analysis------------------------------
mkdir ./Skytrax_2016-2019_data_selection/Output
mkdir ./DataPreprocessing/Output
mkdir ./DataPreprocessing/Output/Boxplots
mkdir ./DataTransformation/CustomerRecommendationTask/Output
mkdir ./DataTransformation/OverallRatingTask/Output
mkdir ./DataTransformation/AirlineLeisureRatingsTask/Output
mkdir ./DataMining/CustomerRecommendationTask/Output
mkdir ./DataMining/OverallRatingTask/Output
mkdir ./DataMining/AirlineLeisureRatingsTask/Output
# Run data selection 
python ./Skytrax_2016-2019_data_selection/dataSelection.py 

# Run data pre-processing 
python ./DataPreprocessing/dataPreprocessing.py 

# Data transformation 
# Step 1: Run customer recommendation task
python ./DataTransformation/CustomerRecommendationTask/crTransformation.py

# Step 2: Run overall rating task
python ./DataTransformation/OverallRatingTask/orTransformation.py

# Step 3: Run airline leisure rating task
python ./DataTransformation/AirlineLeisureRatingsTask/alTransformation.py

# Data mining
# Step 1: Run customer recommendation task mapper
cat ./DataTransformation/CustomerRecommendationTask/Output/customer_recommendation_analysis.txt | python ./DataMining/CustomerRecommendationTask/crMapper.py > ./DataMining/CustomerRecommendationTask/Output/crMapperOutput.txt 

# Step 2: Run customer recommendation task reducer
cat ./DataMining/CustomerRecommendationTask/Output/crMapperOutput.txt | sort | python ./DataMining/CustomerRecommendationTask/crReducer.py > ./DataMining/CustomerRecommendationTask/Output/crReducerOutput.txt 

# Step 3: Run overall rating task
python ./DataMining/OverallRatingTask/orDataMining.py

# Step 4: Run 
python ./DataMining/AirlineLeisureRatingsTask/alDataMining.py

# End of analysis flow
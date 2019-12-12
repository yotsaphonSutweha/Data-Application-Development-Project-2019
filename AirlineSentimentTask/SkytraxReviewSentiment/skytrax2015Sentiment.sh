mkdir output

# Pre-processing task for only getting the customer comments column
python skytrax2015Preprocessing.py > output/skyTrax2015PreprocessOutputs.txt

# Using the Mapper to produce the results of sentiment score for each customer comment
cat output/skyTrax2015PreprocessOutputs.txt | python sentimentMapper.py > output/skyTrax2015SentimentMapperOutputs.txt

# Using the Reducer to produce the overall sentiment scores for the Skytrax 2015 dataset 
cat output/skyTrax2015SentimentMapperOutputs.txt | python sentimentReducer.py > output/skyTrax2015SentimentReducerOutputs.txt 
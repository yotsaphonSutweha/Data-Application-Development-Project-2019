mkdir Output 

cat ../../DataTransformation/CustomerRecommendationTask/Output/customer_recommendation_analysis.txt | python crMapper.py > Output/crMapperOutput.txt 

cat Output/crMapperOutput.txt | sort | python crReducer.py > Output/crReducerOutput.txt 
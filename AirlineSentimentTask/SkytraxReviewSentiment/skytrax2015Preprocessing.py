import pandas as pd
dataset = pd.read_csv("../../skytrax_reviews_delta_2015_cleaning.csv")
customerComments = dataset['review_comment']
comments = []

for comment in customerComments:
    # strip white spaces
    comment = comment.strip()
    # take out quotes before and after the review title
    comment = comment.replace('"', '')
    comments.append(comment)

for customerComment in comments:
    print(customerComment)
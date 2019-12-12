mkdir Output

python deltaTweetCleaning.py > Output/deltaTweetCleaningOutput.txt

python deltaTweetDataSelection.py > Output/deltaTweetDataSelectionOutput.txt

cat Output/deltaTweetDataSelectionOutput.txt | python deltaTweetTransformation.py > Output/deltaTweetTransformationOutput.txt

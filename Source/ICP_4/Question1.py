import pandas as pd

# read the processed csv
dataframe = pd.read_csv('train_preprocessed.csv')

# this prints a general correlation between survival and sex
print(dataframe['Survived'].corr(dataframe['Sex']))
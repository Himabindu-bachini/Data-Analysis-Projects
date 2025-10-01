# data_cleaning.py

import pandas as pd

# Load dataset
df = pd.read_csv('your_dataset.csv')

# Check for missing values
print(df.isnull().sum())

# Fill missing values or drop rows/columns
df.fillna(0, inplace=True)

# Save cleaned data
df.to_csv('cleaned_dataset.csv', index=False)

import pandas as pd

# Load data
df = pd.read_csv('construction_budget_data.csv')

# Display the first few rows of the dataset
print(df.head())

# Basic data cleaning
df.info()
df.describe()

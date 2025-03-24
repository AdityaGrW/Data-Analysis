# data_cleaning.ipynb
import pandas as pd

# Load raw data
file_path = 'data/raw/nba_data.csv'
data = pd.read_csv(file_path)

# Function to clean data
def clean_data(data):
    # Example cleaning steps
    data = data.dropna()  # Drop missing values
    data = data[data['column_name'] > 0]  # Filter data
    return data

# Clean the data
cleaned_data = clean_data(data)

# Save the cleaned data
cleaned_data.to_csv('data/cleaned/nba_cleaned_data.csv', index=False)

# Display the first few rows of the cleaned data
cleaned_data.head()

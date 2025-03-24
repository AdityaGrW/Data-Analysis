# data_extraction.ipynb
import pandas as pd

# Function to extract data
def extract_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Load data from a CSV file
file_path = 'data/raw/nba_data.csv'
data = extract_data(file_path)

# Display the first few rows of the data
data.head()

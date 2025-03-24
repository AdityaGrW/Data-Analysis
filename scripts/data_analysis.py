# data_analysis.ipynb
import pandas as pd

# Load cleaned data
file_path = 'data/cleaned/nba_cleaned_data.csv'
data = pd.read_csv(file_path)

# Function to analyze data
def analyze_data(data):
    # Example analysis: summary statistics
    summary_stats = data.describe()
    return summary_stats

# Analyze the data
analysis_results = analyze_data(data)

# Display analysis results
analysis_results

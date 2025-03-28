"""# **Download latest version kraggle dictonery **"""
import kagglehub

# give path
path = kagglehub.dataset_download("joebeachcapital/nba-player-statistics")

print("Path to dataset files:", path)

"""# **Loading the list**"""

import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the name
file_name = "nba_data_processed.csv"

# Load the latest version
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "joebeachcapital/nba-player-statistics",
  file_name,
  )

print( df)

"""**Cleaning the repeated players from the list**"""

import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Download the dataset if it hasn't been already.
path = kagglehub.dataset_download("joebeachcapital/nba-player-statistics")

# Set the name
file_name = "nba_data_processed.csv"

# Construct the full file path
file_path = f"{path}/{file_name}" # Build the full path to the CSV file.

# Load the DataFrame using the full file path
df = pd.read_csv(file_path) # Use the full path when loading the dataframe.

# Select only numerical columns for calculating the mean
numeric_cols = df.select_dtypes(include=['number']).columns # Get a list of numerical columns

# Group by player and calculate the average of all numerical columns
player_avg = df.groupby('Player')[numeric_cols].mean()

# Reset the index to make 'Player' a regular column
cleaned_df = player_avg.reset_index()

# Now 'cleaned_df' contains the average statistics for each player
print(cleaned_df)

"""**Checking cleaning function**"""

import pandas as pd
# Assuming 'df' is your loaded DataFrame from 'nba_data_processed.csv'.
filtered_df = cleaned_df[cleaned_df['Player'] == 'Yuki Kawamura']
print( filtered_df)

"""**Downloading the csv file**"""

from google.colab import files

# downloading new  and cleaned NBA data file
cleaned_df.to_csv('cleaned_nba_data.csv', index=False)
files.download('cleaned_nba_data.csv')

from IPython.display import display
df = pd.read_csv('cleaned_nba_data.csv')
display(df)

"""# **Power bi**"""

!pip install powerbiclient
from powerbiclient import Report, models
from powerbiclient.authentication import DeviceCodeLoginAuthentication

   # Initialize device flow authentication
device_auth = DeviceCodeLoginAuthentication()


# Data-Analysis
A Data Analysis Project on Analyzing the data of NBA players from season 2022-2023 . The project focuses on extracting, cleaning, analyzing, and visualizing NBA data to gain insights into player and team performance.

# Basketball Data Analysis Project

## 1. Project Overview
This project aims to provide a comprehensive analysis of basketball data, focusing on player and team performance. By leveraging web scraping, data manipulation, and visualization techniques, the project delivers insights into key performance indicators, trends, and patterns within the data.

## 2. Key Features
* **Data Acquisition**: Automated data collection from Basketball-Reference.com using Python web scraping.
* **Data Cleaning & Preprocessing**: Robust data cleaning and transformation using Python and Pandas.
* **Exploratory Data Analysis (EDA)**: In-depth analysis of player and team statistics using Jupyter Notebooks.
* **Interactive Visualizations**: Creation of interactive dashboards using Tableau.
* **Reproducible Workflow**: Well-structured repository with scripts and notebooks for reproducibility.

## 3. Technologies Used
* Python
* Pandas
* Beautiful Soup
* Requests
* Tableau

## 4. Project Structure
*Data Acquisition
*Data Cleaning & Preprocessing
*Interactive Visualizations
*reating dash-boards

## 5. Getting Started

### 5.1 Prerequisites
* Python 3.x
* Pip
* Tableau Desktop

### 5.2 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/basketball-data-analysis.git](https://www.google.com/search?q=https://github.com/your-username/basketball-data-analysis.git)
    cd basketball-data-analysis
    ```
2.  **Set up a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### 5.3 Data Acquisition
* Run the data acquisition script:
    ```bash
    python scripts/scrape_data.py
    ```
* The raw data will be saved in the `data/raw/` directory.

### 5.4 Data Analysis
* Open the Jupyter Notebooks in the `notebooks/` directory.
* Follow the notebooks sequentially:
    1.  `01_data_acquisition.ipynb`: For data collection.
    2.  `02_data_cleaning.ipynb`: For data cleaning and preprocessing.
    3.  `03_exploratory_data_analysis.ipynb`: For data analysis.
    4.  `04_data_visualization.ipynb`: For creating visualizations.

### 5.5 Visualization
* Open the `Basketball_Dashboard.twb` file in Tableau Desktop.

## 6. Data Sources
* [Basketball-Reference.com](https://www.basketball-reference.com/)

## 7. Key Metrics
* Total Points
* Total Assists
* Contribution Score (Weighted)

## 8. Contributions
* Feel free to contribute to this project by submitting pull requests or opening issues.

## 9. License
* [MIT License](LICENSE)

"""
Demographic Data Pipeline

Description:
This Python program performs a full data pipeline for demographic data by zip code. The data is sourced from a CSV file
and undergoes the following steps:

1. Data Ingestion:
   - The program reads the demographic data from a provided CSV file.
   - The data is loaded into a Pandas DataFrame for further processing.

2. Data Storage:
   - The ingested data is saved locally in a CSV file to ensure data persistence and for later access.

3. Data Cleansing and Preprocessing:
   - The program handles missing values using forward-fill method.
   - It ensures that 'TotalPopulation' values of zero are treated as missing and removes such records.
   - The program replaces infinite values with NaN to ensure data consistency.

4. Kidney Disease Analysis:
   - The program analyzes which states have higher rates of kidney disease.
   - Visualizations are created to depict the distribution of kidney disease rates by state.

Author: Antoine Gaton
Email: antoine.gaton@student.ctuonline.edu
Date: July 14, 2024
"""
import pandas as pd  # Importing pandas for data manipulation
import numpy as np  # Importing numpy for numerical operations
import matplotlib.pyplot as plt  # Importing matplotlib for plotting
import seaborn as sns  # Importing seaborn for statistical data visualization
import warnings  # Importing warnings to handle warning messages
import os  # Importing os for file path operations
import webbrowser  # Importing webbrowser to open files in the default browser

# Suppress the specific FutureWarning from seaborn
warnings.filterwarnings("ignore", category=FutureWarning, module="seaborn")

# Step 1: Ingest the Data
data_url = 'https://data.cdc.gov/api/views/mssc-ksj7/rows.csv?accessType=DOWNLOAD'  # URL for the data
df = pd.read_csv(data_url)  # Reading the data into a pandas DataFrame

# Print the columns of the DataFrame
print("Columns in the dataset:", df.columns)
print("-------------------------------------------------------------------------------------------")

# Print columns related to kidney disease
kidney_disease_columns = [col for col in df.columns if 'KIDNEY' in col.upper()]
print("Columns related to kidney disease:", kidney_disease_columns)
print("-------------------------------------------------------------------------------------------")

# Also print the first few rows to understand the data
print(df.head())
print("-------------------------------------------------------------------------------------------")

# Step 2: Store the Data
df.to_csv('demographics_data.csv', index=False)  # Saving the DataFrame to a CSV file

# Step 3: Cleansing and Preprocessing
df.ffill(inplace=True)  # Handle missing values using forward fill method

# Ensure 'TotalPopulation' values of zero are treated as missing and remove such records
df['TotalPopulation'] = df['TotalPopulation'].apply(lambda x: np.nan if x == 0 else x)  # Replace 0 values with NaN
df.dropna(subset=['TotalPopulation'], inplace=True)  # Drop rows where 'TotalPopulation' is NaN

# Convert any infinite values to NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)  # Replace infinite values with NaN

# Step 4: Kidney Disease Analysis
# Use 'StateDesc' for state names and 'KIDNEY_CrudePrev' for kidney disease rates
if 'KIDNEY_CrudePrev' in df.columns and 'StateDesc' in df.columns:  # Check if necessary columns exist
    state_kidney_disease = df.groupby('StateDesc')['KIDNEY_CrudePrev'].mean().reset_index()  # Group by state and calculate mean

    # Sort by kidney disease rate
    state_kidney_disease.sort_values(by='KIDNEY_CrudePrev', ascending=False, inplace=True)

    # Visualize kidney disease rates by state
    plt.figure(figsize=(12, 8))  # Set the figure size
    sns.barplot(x='KIDNEY_CrudePrev', y='StateDesc', data=state_kidney_disease, palette='viridis')  # Create a bar plot
    plt.title('Average Kidney Disease Rate by State')  # Set the title
    plt.xlabel('Kidney Disease Rate (Crude)')  # Set the x-axis label
    plt.ylabel('State')  # Set the y-axis label
    kidney_disease_file = 'kidney_disease_by_state.png'  # Filename for the plot
    plt.savefig(kidney_disease_file)  # Save the plot to a file
    plt.show()  # Display the plot

    # Open the kidney disease rate plot
    webbrowser.open('file://' + os.path.realpath(kidney_disease_file))  # Open the saved plot
else:
    print("The required columns 'KIDNEY_CrudePrev' and 'StateDesc' are not present in the data.")

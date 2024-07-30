"""
Script for COVID-19 Daily Counts Prediction Using K-Nearest Neighbors (KNN)

Description:
This script demonstrates the implementation of a predictive analytics algorithm using the K-Nearest Neighbors (KNN) algorithm in Python. The script utilizes a dataset of COVID-19 daily counts of cases, hospitalizations, and deaths to create a predictive model. The dataset is preprocessed to handle date features and imbalanced classes. The dataset is split into training and testing sets, with 70% used for training and 30% used for testing. SMOTE is applied to handle class imbalance in the training set. The results of the prediction are evaluated and displayed, including accuracy, a classification report, and a confusion matrix.

Author: Antoine Gaton
Email: antoine.gaton@student.ctuonline.edu
Date: July 7, 2024

Dependencies:
- pandas
- scikit-learn
- imbalanced-learn

Usage:
1. Ensure you have Python installed on your system.
2. Install the required libraries:
   pip install pandas scikit-learn imbalanced-learn
3. Run the script:
   unit4.py

Dataset:
- The dataset contains daily counts of COVID-19 cases, hospitalizations, and deaths.

Data Preprocessing:
- The date column is converted to datetime format, and year, month, and day are extracted as separate features.
- The target variable (CASE_COUNT) is binned into categories for classification.
- SMOTE is used to handle class imbalance in the training set.

Model Evaluation:
- The model's accuracy, precision, recall, F1-score, and confusion matrix are outputted to evaluate performance.
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE

# Load the dataset
data = pd.read_csv(r"C:\Users\antoi\OneDrive\Documents\Coding\CTU\Foundation_of_Big_Data_Analytics\COVID-19_Daily_Counts_of_Cases__Hospitalizations__and_Deaths.csv")

# Convert date column to datetime
data['date_of_interest'] = pd.to_datetime(data['date_of_interest'], format='%m/%d/%Y')

# Extract numerical features from the date column
data['year'] = data['date_of_interest'].dt.year
data['month'] = data['date_of_interest'].dt.month
data['day'] = data['date_of_interest'].dt.day

# Drop the original date column
data.drop(columns=['date_of_interest'], inplace=True)

# Binning the CASE_COUNT into categories: 0 (low), 1 (medium), 2 (high), 3 (very high)
y = pd.cut(data['CASE_COUNT'], bins=[-1, 100, 500, 1000, float('inf')], labels=[0, 1, 2, 3])
X = data.drop(columns=['CASE_COUNT'])

# Check class distribution
print('---------------------------------------------\n')
print(y.value_counts())
print('\n---------------------------------------------\n')

# Split the dataset into training (70%) and testing (30%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Resample the training data using SMOTE to handle class imbalance
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Initialize the KNN model with k=5
knn = KNeighborsClassifier(n_neighbors=5)

# Train the model using the resampled training data
knn.fit(X_train_resampled, y_train_resampled)

# Make predictions on the test set
y_pred = knn.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
print('\n---------------------------------------------\n')

# Detailed classification report with zero_division parameter
report = classification_report(y_test, y_pred, zero_division=1)
print('Classification Report:')
print(report)
print('---------------------------------------------\n')

# Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:')
print(conf_matrix)
print('\n---------------------------------------------\n')
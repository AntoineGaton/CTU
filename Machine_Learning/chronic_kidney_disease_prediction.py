# -*- coding: utf-8 -*-
"""Chronic Kidney Disease Prediction

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ao47rJbtQLkJHShh_bOATYZq6iHzHMKr
"""

pip install ucimlrepo

"""
Name: Antoine Gaton
Date: October 20, 2024
Course: CS379
Description: This Python script implements a machine learning solution for predicting chronic kidney disease using logistic regression. It fetches the Chronic Kidney Disease dataset from the UCI Machine Learning Repository, preprocesses the data, trains a logistic regression model, and evaluates its performance. The script also includes visualizations of the confusion matrix and feature importance to aid in interpreting the results.
GitHub Link: https://github.com/AntoineGaton/CTU/blob/main/Chronic_Kidney_Disease_Prediction.ipynb
"""

# Import necessary libraries
import pandas as pd  # For data manipulation and analysis
import numpy as np  # For numerical operations
from ucimlrepo import (
    fetch_ucirepo,
)  # To fetch datasets from UCI Machine Learning Repository
from sklearn.model_selection import (
    train_test_split,
)  # For splitting data into training and testing sets
from sklearn.preprocessing import StandardScaler  # For feature scaling
from sklearn.impute import SimpleImputer  # For handling missing values
from sklearn.linear_model import LogisticRegression  # Our machine learning model
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)  # For model evaluation
import matplotlib.pyplot as plt  # For creating static plots
import seaborn as sns  # For creating statistical graphics
from rich.console import (
    Console,
)  # For creating rich text and beautiful formatting in the terminal
from rich.table import Table  # For creating tables in the terminal
from rich.panel import Panel  # For creating panels in the terminal
from rich.text import Text  # For styling text in the terminal
from google.colab import files


# Initialize Rich console for pretty printing
console = Console()

# Fetch the Chronic Kidney Disease dataset from UCI Machine Learning Repository
# This dataset contains various medical predictors and a target variable indicating the presence of kidney disease
chronic_kidney_disease = fetch_ucirepo(id=336)

# Extract features (X) and target variable (y) from the dataset
# Features are the input variables we'll use to predict the target
X = (
    chronic_kidney_disease.data.features.copy()
)  # Create a copy to avoid modifying the original data
y = chronic_kidney_disease.data.targets.copy()

# Print dataset metadata
console.print(Panel.fit("[bold cyan]Dataset Metadata", style="cyan"))
console.print(chronic_kidney_disease.metadata)

# Print information about each variable in the dataset
console.print(Panel.fit("[bold cyan]Variable Information", style="cyan"))
table = Table(show_header=True, header_style="bold magenta")
for col in chronic_kidney_disease.variables.columns:
    table.add_column(col, style="dim")
for _, row in chronic_kidney_disease.variables.iterrows():
    table.add_row(*[str(x) for x in row])
console.print(table)

# Preprocess the data
# Convert categorical variables to numeric
# Machine learning models require numerical input, so we need to encode categorical variables
categorical_columns = X.select_dtypes(include=["object"]).columns
for col in categorical_columns:
    X.loc[:, col] = pd.Categorical(X[col]).codes

# Handle missing values
# We'll use mean imputation, which replaces missing values with the mean of the column
imputer = SimpleImputer(strategy="mean")
X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

# Split the data into training and testing sets
# This allows us to evaluate our model on data it hasn't seen during training
X_train, X_test, y_train, y_test = train_test_split(
    X_imputed, y, test_size=0.2, random_state=42
)

# Scale the features
# This ensures that all features are on a similar scale, which is important for many machine learning algorithms
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train the logistic regression model
# Logistic regression is a good starting point for binary classification problems
model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train.values.ravel())

# Make predictions on the test set
y_pred = model.predict(X_test_scaled)

# Calculate accuracy
# Accuracy is the proportion of correct predictions (both true positives and true negatives) among the total number of cases examined
accuracy = accuracy_score(y_test, y_pred)
console.print(Panel(f"[bold green]Accuracy: {accuracy:.2f}", expand=False))

# Print classification report
# This report shows the main classification metrics for each class
console.print(Panel.fit("[bold cyan]Classification Report", style="cyan"))
report = classification_report(y_test, y_pred, output_dict=True)
table = Table(show_header=True, header_style="bold magenta")
table.add_column("Class", style="dim")
table.add_column("Precision", style="dim")
table.add_column("Recall", style="dim")
table.add_column("F1-score", style="dim")
table.add_column("Support", style="dim")
for class_name, metrics in report.items():
    if class_name not in ["accuracy", "macro avg", "weighted avg"]:
        table.add_row(
            class_name,
            f"{metrics['precision']:.2f}",
            f"{metrics['recall']:.2f}",
            f"{metrics['f1-score']:.2f}",
            str(metrics["support"]),
        )
console.print(table)

# Create confusion matrix
# A confusion matrix shows the number of correct and incorrect predictions made by the classification model
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("confusion_matrix.png")
plt.close()

# Calculate and visualize feature importance
# This shows which features have the biggest impact on the model's predictions
feature_importance = pd.DataFrame(
    {"feature": X.columns, "importance": abs(model.coef_[0])}
)
feature_importance = feature_importance.sort_values("importance", ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x="importance", y="feature", data=feature_importance)
plt.title("Feature Importance")
plt.xlabel("Absolute Coefficient Value")
plt.tight_layout()
plt.savefig("feature_importance.png")
plt.close()

# Display the saved images in Colab
from IPython.display import Image, display

console.print(Panel.fit("[bold green]Displaying saved visualizations", style="green"))

console.print("[cyan]Confusion Matrix:[/cyan]")
display(Image(filename="confusion_matrix.png"))

console.print("[cyan]Feature Importance:[/cyan]")
display(Image(filename="feature_importance.png"))

files.download('confusion_matrix.png')

files.download('feature_importance.png')
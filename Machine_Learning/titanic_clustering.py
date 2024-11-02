"""
Name: Antoine Gaton
Date: October 13, 2024
Course, CS491
Description: Titanic Dataset Clustering using KMeans (Unsupervised Learning)
"""

# Importing necessary libraries
import pandas as pd  # For data manipulation and analysis
import numpy as np  # For numerical operations
from sklearn.preprocessing import StandardScaler  # For standardizing features
from sklearn.cluster import KMeans  # For K-means clustering
from rich.console import Console  # For enhanced console output
from rich.table import Table  # For creating tables in the console
from rich.panel import Panel  # For creating panels in the console

# Create a Console object for rich output
console = Console()


def load_and_preprocess_data(url):
    """
    Load the Titanic dataset and preprocess it for clustering.

    This function performs several data cleaning and preprocessing steps:
    1. Load the data from a URL
    2. Remove irrelevant columns
    3. Handle missing values
    4. Encode categorical variables
    """
    # Load the dataset from the URL
    data = pd.read_csv(url)

    # Drop columns that are not useful for clustering analysis
    data = data.drop(columns=["Name", "Ticket", "Cabin"])

    # Fill missing values in the 'Age' column with the median age
    data["Age"] = data["Age"].fillna(data["Age"].median())

    # Fill missing values in the 'Embarked' column with the most common value
    data["Embarked"] = data["Embarked"].fillna(data["Embarked"].mode()[0])

    # Convert 'Sex' to numerical values (0 for male, 1 for female)
    data["Sex"] = data["Sex"].map({"male": 0, "female": 1})

    # Create dummy variables for 'Embarked' column (one-hot encoding)
    data = pd.get_dummies(data, columns=["Embarked"], drop_first=True)

    return data


def perform_clustering(data):
    """
    Perform K-means clustering on the dataset.

    This function:
    1. Standardizes the features
    2. Applies K-means clustering with 2 clusters
    3. Adds the cluster labels to the dataset
    """
    # Standardize the features (important for K-means)
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data.drop(columns=["Survived"]))

    # Perform K-means clustering with 2 clusters
    kmeans = KMeans(n_clusters=2, random_state=42)
    data["Cluster"] = kmeans.fit_predict(scaled_data)

    return data


def describe_clusters(data):
    """
    Describe the clusters by showing the mean values of features for each cluster.

    This function creates a table to display the cluster descriptions.
    """
    # Calculate mean values for each cluster
    cluster_description = data.groupby("Cluster").mean()

    # Create a table to display the cluster description
    table = Table(title="Cluster Description")

    # Add columns to the table
    for column in cluster_description.columns:
        table.add_column(column, justify="right", style="cyan", no_wrap=True)

    # Add rows to the table
    for index, row in cluster_description.iterrows():
        table.add_row(*[f"{value:.2f}" for value in row])

    # Print the table in a panel
    console.print(Panel(table, expand=False))


def main():
    """
    Main function to orchestrate the Titanic dataset clustering analysis.

    This function:
    1. Loads and preprocesses the data
    2. Performs clustering
    3. Describes the clusters
    """
    console.print(
        Panel(
            "[bold cyan]Titanic Dataset Clustering Analysis[/bold cyan]", expand=False
        )
    )

    # URL of the Titanic dataset
    url = (
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    )

    # Load and preprocess the data
    with console.status("[bold green]Loading and preprocessing data...[/bold green]"):
        data = load_and_preprocess_data(url)
    console.print("[bold green]Data loaded and preprocessed successfully![/bold green]")

    # Perform clustering
    with console.status("[bold green]Performing clustering...[/bold green]"):
        data = perform_clustering(data)
    console.print("[bold green]Clustering completed![/bold green]")

    # Describe the clusters
    describe_clusters(data)


# Run the script
if __name__ == "__main__":
    main()

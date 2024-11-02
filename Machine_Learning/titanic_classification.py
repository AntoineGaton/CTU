"""
Name: Antoine Gaton
Date: October 13, 2024
Course, CS491
Description: Titanic Dataset Classification with Logistic Regression and Random Forest (Supervised Learning)
"""

# Importing necessary libraries
import pandas as pd  # For data manipulation and analysis
import numpy as np  # For numerical operations
from sklearn.model_selection import (
    train_test_split,
)  # For splitting data into training and testing sets
from sklearn.preprocessing import StandardScaler  # For standardizing features
from sklearn.ensemble import RandomForestClassifier  # For Random Forest classification
from sklearn.linear_model import LogisticRegression  # For Logistic Regression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
)  # For model evaluation
from rich.console import Console  # For enhanced console output
from rich.table import Table  # For creating tables in the console
from rich.panel import Panel  # For creating panels in the console

# Create a Console object for rich output
console = Console()


def load_and_preprocess_data(url):
    """
    Load the Titanic dataset and preprocess it for classification.

    This function performs several data cleaning and preprocessing steps:
    1. Load the data from a URL
    2. Remove irrelevant columns
    3. Handle missing values
    4. Encode categorical variables
    """
    # Load the dataset from the URL
    data = pd.read_csv(url)

    # Drop columns that are not useful for our analysis
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


def split_data(data):
    """
    Split the data into features (X) and target variable (y),
    then further split into training and testing sets.
    """
    # Separate features (X) and target variable (y)
    X = data.drop(columns=["Survived"])
    y = data["Survived"]

    # Split data into training (80%) and testing (20%) sets
    return train_test_split(X, y, test_size=0.2, random_state=42)


def logistic_regression_model(X_train, X_test, y_train, y_test):
    """
    Train a Logistic Regression model, make predictions, and display the results.

    This function:
    1. Trains a Logistic Regression model
    2. Makes predictions on the test set
    3. Calculates and displays the accuracy and classification report
    """
    # Create and train the Logistic Regression model
    log_reg = LogisticRegression(max_iter=1000, random_state=42)
    log_reg.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred_log_reg = log_reg.predict(X_test)

    # Calculate accuracy
    accuracy_log_reg = accuracy_score(y_test, y_pred_log_reg)

    # Generate classification report
    report_log_reg = classification_report(y_test, y_pred_log_reg, output_dict=True)

    # Display results
    console.print(Panel("[bold]Logistic Regression Model[/bold]", expand=False))
    console.print(
        f"Accuracy with Logistic Regression: [green]{accuracy_log_reg:.4f}[/green]"
    )

    # Create a table for the classification report
    table = Table(title="Classification Report for Logistic Regression")
    table.add_column("Metric", style="cyan")
    table.add_column("Precision", justify="right")
    table.add_column("Recall", justify="right")
    table.add_column("F1-Score", justify="right")
    table.add_column("Support", justify="right")

    # Add rows to the table
    for class_name, metrics in report_log_reg.items():
        if class_name in ["0", "1"]:
            table.add_row(
                f"Class {class_name}",
                f"{metrics['precision']:.2f}",
                f"{metrics['recall']:.2f}",
                f"{metrics['f1-score']:.2f}",
                str(metrics["support"]),
            )

    # Print the table
    console.print(Panel(table, expand=False))


def random_forest_model(X_train, X_test, y_train, y_test):
    """
    Train a Random Forest model, make predictions, and display the results.

    This function:
    1. Trains a Random Forest model
    2. Makes predictions on the test set
    3. Calculates and displays the accuracy and classification report
    """
    # Create and train the Random Forest model
    classifier = RandomForestClassifier(random_state=42)
    classifier.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred_rf = classifier.predict(X_test)

    # Calculate accuracy
    accuracy_rf = accuracy_score(y_test, y_pred_rf)

    # Generate classification report
    report_rf = classification_report(y_test, y_pred_rf, output_dict=True)

    # Display results
    console.print(Panel("[bold]Random Forest Model[/bold]", expand=False))
    console.print(f"Accuracy with RandomForest: [green]{accuracy_rf:.4f}[/green]")

    # Create a table for the classification report
    table = Table(title="Classification Report for Random Forest")
    table.add_column("Metric", style="cyan")
    table.add_column("Precision", justify="right")
    table.add_column("Recall", justify="right")
    table.add_column("F1-Score", justify="right")
    table.add_column("Support", justify="right")

    # Add rows to the table
    for class_name, metrics in report_rf.items():
        if class_name in ["0", "1"]:
            table.add_row(
                f"Class {class_name}",
                f"{metrics['precision']:.2f}",
                f"{metrics['recall']:.2f}",
                f"{metrics['f1-score']:.2f}",
                str(metrics["support"]),
            )

    # Print the table in a panel
    console.print(Panel(table, expand=False))


def main():
    """
    Main function to orchestrate the Titanic dataset classification analysis.

    This function:
    1. Loads and preprocesses the data
    2. Splits the data into training and testing sets
    3. Trains and evaluates Logistic Regression and Random Forest models
    """
    console.print(
        Panel("[bold cyan]Titanic Dataset Classification[/bold cyan]", expand=False)
    )

    # URL of the Titanic dataset
    url = (
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    )

    # Load and preprocess the data
    with console.status("[bold green]Loading and preprocessing data...[/bold green]"):
        data = load_and_preprocess_data(url)
    console.print("[bold green]Data loaded and preprocessed successfully![/bold green]")

    # Split the data into training and testing sets
    with console.status(
        "[bold green]Splitting data for model training...[/bold green]"
    ):
        X_train, X_test, y_train, y_test = split_data(data)
    console.print("[bold green]Data split completed![/bold green]")

    # Train and evaluate the Logistic Regression model
    logistic_regression_model(X_train, X_test, y_train, y_test)

    # Train and evaluate the Random Forest model
    random_forest_model(X_train, X_test, y_train, y_test)


# Call the main function to run the script
if __name__ == "__main__":
    main()

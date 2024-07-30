"""
Script for Text Preprocessing and TF-IDF Analysis

Description:
This script loads a dataset containing text data, preprocesses the text by removing punctuation,
converting to lowercase, and removing stopwords. It then calculates the Term Frequency-Inverse
Document Frequency (TF-IDF) for the text data and saves the results to a new CSV file.

Author: Antoine Gaton
Email: antoine.gaton@student.ctuonline.edu
Date: June 23, 2024

Dependencies:
- pandas
- scikit-learn
- nltk

Usage:
1. Ensure you have the required libraries installed:
   pip install pandas scikit-learn nltk
2. Place the dataset in the specified path.
3. Run the script:
   python unit2.py

Dataset:
- Tweets.csv: Contains text data for sentiment analysis from the Airline Sentiment dataset.
  Source: https://www.kaggle.com/welkin10/airline-sentiment
"""
# Import pandas for data manipulation and analysis
import pandas as pd

# Import TfidfVectorizer from scikit-learn for TF-IDF calculations
from sklearn.feature_extraction.text import TfidfVectorizer

# Import nltk for natural language processing
import nltk

# Import stopwords from NLTK
from nltk.corpus import stopwords

# Import string for string operations (like removing punctuation)
import string

# Download stopwords from NLTK (needed for text preprocessing)
nltk.download('stopwords')

# Define the path to your dataset
data_path = r"C:\Users\antoi\OneDrive\Documents\Coding\CTU\Foundation_of_Big_Data_Analytics\Tweets.csv"

# Load the dataset into a pandas DataFrame
df = pd.read_csv(data_path)

# Function to preprocess text
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))  # Get the set of English stopwords
    # Remove punctuation from the text
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Convert text to lowercase
    text = text.lower()
    # Split the text into words
    words = text.split()
    # List to hold words after removing stopwords
    filtered_words = []
    
    for word in words:
        # Check if the word is not a stopword
        if word not in stop_words:
            filtered_words.append(word)
    
    # Join the filtered words back into a single string
    cleaned_text = ' '.join(filtered_words)
    
    return cleaned_text

# Apply the preprocessing function to the 'text' column in the DataFrame
df['cleaned_text'] = df['text'].apply(preprocess_text)

# Initialize the TF-IDF Vectorizer
# max_features=100 limits the number of features (words) to the top 100 by TF-IDF score
vectorizer = TfidfVectorizer(max_features=100)

# Fit and transform the cleaned text data into a TF-IDF matrix
tfidf_matrix = vectorizer.fit_transform(df['cleaned_text'])

# Convert the TF-IDF matrix to a DataFrame for better readability
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())

# Combine the original DataFrame with the new TF-IDF DataFrame
result_df = pd.concat([df, tfidf_df], axis=1)

# Save the resulting DataFrame to a new CSV file
result_df.to_csv('airline_sentiment_with_tfidf.csv', index=False)
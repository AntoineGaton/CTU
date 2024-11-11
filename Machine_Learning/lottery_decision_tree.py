"""
Name: Lottery Decision Tree Analysis
Date: November 10, 2024
Course: CS379
Description: Enhanced implementation of a decision tree classifier using Gini impurity
            to analyze Powerball lottery patterns. Includes cross-validation,
            hyperparameter tuning, and multiple evaluation metrics.
"""

import numpy as np
import pandas as pd
from collections import Counter
from typing import List, Dict, Tuple, Union
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score
from sklearn.tree import DecisionTreeClassifier

class Node:
   """
   Represents a node in the decision tree.
   
   Attributes:
      feature (int): Index of the feature used for splitting
      threshold (float): Value used for splitting
      left (Node): Left child node
      right (Node): Right child node
      value (Any): Predicted class (for leaf nodes)
   """
   def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
      self.feature = feature
      self.threshold = threshold
      self.left = left
      self.right = right
      self.value = value

class PowerballDecisionTree:
   """
   Decision Tree Classifier specialized for Powerball analysis.
   
   Attributes:
      max_depth (int): Maximum depth of the tree
      min_samples_split (int): Minimum samples required to split a node
      root (Node): Root node of the tree
   """
   
   def __init__(self, max_depth=3, min_samples_split=2):
      self.max_depth = max_depth
      self.min_samples_split = min_samples_split
      self.root = None
      
   def _gini_impurity(self, y: np.ndarray) -> float:
      """
      Calculate Gini impurity for a set of labels.

      Parameters:
            y (np.ndarray): Array of target labels

      Returns:
            float: Gini impurity value between 0 (pure) and 1 (impure)
      """
      if len(y) == 0:
            return 0
      
      counts = Counter(y)
      probabilities = [count/len(y) for count in counts.values()]
      gini = 1 - sum([p**2 for p in probabilities])
      return gini

   def _best_split(self, X: np.ndarray, y: np.ndarray) -> Tuple[int, float]:
      """Find the best split using Gini impurity"""
      best_gini = float('inf')
      best_feature = None
      best_threshold = None
      
      n_features = X.shape[1]
      
      for feature in range(n_features):
            thresholds = np.unique(X[:, feature])
            
            for threshold in thresholds:
               left_mask = X[:, feature] <= threshold
               right_mask = ~left_mask
               
               if np.sum(left_mask) == 0 or np.sum(right_mask) == 0:
                  continue
               
               left_gini = self._gini_impurity(y[left_mask])
               right_gini = self._gini_impurity(y[right_mask])
               
               # Weighted average of Gini impurity
               n_left = np.sum(left_mask)
               n_right = np.sum(right_mask)
               gini = (n_left * left_gini + n_right * right_gini) / len(y)
               
               if gini < best_gini:
                  best_gini = gini
                  best_feature = feature
                  best_threshold = threshold
                  
      return best_feature, best_threshold
   
   def _build_tree(self, X: np.ndarray, y: np.ndarray, depth: int) -> Node:
      """Recursively build the decision tree"""
      n_samples, n_features = X.shape
      n_classes = len(np.unique(y))
      
      # Stopping criteria
      if (depth >= self.max_depth or 
            n_samples < self.min_samples_split or 
            n_classes == 1):
            leaf_value = Counter(y).most_common(1)[0][0]
            return Node(value=leaf_value)
      
      # Find best split
      feature, threshold = self._best_split(X, y)
      
      if feature is None:
            leaf_value = Counter(y).most_common(1)[0][0]
            return Node(value=leaf_value)
      
      # Create child nodes
      left_mask = X[:, feature] <= threshold
      right_mask = ~left_mask
      
      left = self._build_tree(X[left_mask], y[left_mask], depth + 1)
      right = self._build_tree(X[right_mask], y[right_mask], depth + 1)
      
      return Node(feature=feature, threshold=threshold, left=left, right=right)
   
   def fit(self, X: np.ndarray, y: np.ndarray):
      """Train the decision tree"""
      self.root = self._build_tree(X, y, depth=0)
   
   def _predict_single(self, x: np.ndarray, node: Node) -> int:
      """Make prediction for a single sample"""
      if node.value is not None:
            return node.value
      
      if x[node.feature] <= node.threshold:
            return self._predict_single(x, node.left)
      return self._predict_single(x, node.right)
   
   def predict(self, X: np.ndarray) -> np.ndarray:
      """Make predictions for multiple samples"""
      return np.array([self._predict_single(x, self.root) for x in X])

def load_powerball_data_from_csv(file_path: str) -> Tuple[np.ndarray, np.ndarray]:
   """
   Load and prepare historical Powerball data from a CSV file.

   Parameters:
      file_path (str): Path to the CSV file containing Powerball data

   Returns:
      Tuple[np.ndarray, np.ndarray]: Features array and labels array
   """
   try:
      data = pd.read_csv(file_path)
      # Process data similar to current load_powerball_data function
      # Return processed X, y
      return X, y
   except FileNotFoundError:
      print(f"Error: File {file_path} not found")
      return None, None

def cross_validate(tree: PowerballDecisionTree, X: np.ndarray, y: np.ndarray, k: int = 5) -> float:
   """
   Perform k-fold cross-validation.

   Parameters:
      tree (PowerballDecisionTree): Decision tree model
      X (np.ndarray): Feature array
      y (np.ndarray): Label array
      k (int): Number of folds

   Returns:
      float: Mean accuracy across all folds
   """
   kf = KFold(n_splits=k, shuffle=True, random_state=42)
   accuracies = []

   for train_index, test_index in kf.split(X):
      X_train, X_test = X[train_index], X[test_index]
      y_train, y_test = y[train_index], y[test_index]
      tree.fit(X_train, y_train)
      predictions = tree.predict(X_test)
      accuracy = np.mean(predictions == y_test)
      accuracies.append(accuracy)

   return np.mean(accuracies)

def tune_hyperparameters(X: np.ndarray, y: np.ndarray) -> Tuple[Dict, float]:
   """
   Perform grid search to find optimal hyperparameters.

   Parameters:
      X (np.ndarray): Feature array
      y (np.ndarray): Label array

   Returns:
      Tuple[Dict, float]: Best parameters and corresponding accuracy
   """
   best_accuracy = 0
   best_params = {}

   for max_depth in range(1, 10):
      for min_samples_split in range(2, 10):
            tree = PowerballDecisionTree(max_depth=max_depth, 
                                    min_samples_split=min_samples_split)
            accuracy = cross_validate(tree, X, y)
            if accuracy > best_accuracy:
               best_accuracy = accuracy
               best_params = {
                  'max_depth': max_depth, 
                  'min_samples_split': min_samples_split
               }

   return best_params, best_accuracy

def evaluate_model(predictions: np.ndarray, y_true: np.ndarray) -> Tuple:
   """
   Calculate various performance metrics for the model.

   Parameters:
      predictions (np.ndarray): Predicted labels
      y_true (np.ndarray): True labels

   Returns:
      Tuple: Confusion matrix, precision, recall, and F1 score
   """
   cm = confusion_matrix(y_true, predictions)
   precision = precision_score(y_true, predictions)
   recall = recall_score(y_true, predictions)
   f1 = f1_score(y_true, predictions)
   return cm, precision, recall, f1

def compare_with_sklearn(X_train: np.ndarray, y_train: np.ndarray, 
                        X_test: np.ndarray, y_test: np.ndarray) -> float:
   """
   Compare custom implementation with scikit-learn's DecisionTreeClassifier.

   Parameters:
      X_train, y_train: Training data
      X_test, y_test: Test data

   Returns:
      float: Accuracy of scikit-learn model
   """
   model = DecisionTreeClassifier(criterion='gini', max_depth=3)
   model.fit(X_train, y_train)
   return model.score(X_test, y_test)

def prepare_powerball_features(number: int) -> List[float]:
   """
   Convert a lottery number into meaningful features for analysis.
   
   Parameters:
      number (int): The lottery number to convert
      
   Returns:
      List[float]: List of features including:
            - The number itself
            - Whether it's even/odd (0/1)
            - Last digit
            - First digit(s)
            - Position in range (normalized 0-1)
   """
   return [
      number,                          # The actual number
      number % 2,                      # Even (0) or Odd (1)
      number % 10,                     # Last digit
      number // 10,                    # First digit(s)
      number / 69 if number <= 69 else number / 26  # Normalized position in range
   ]

def main():
   """Main function to run the Powerball analysis"""
   # Generate simulated data
   np.random.seed(42)
   num_drawings = 100
   
   # Generate features and labels
   data = []
   for _ in range(num_drawings):
      # Generate 5 regular numbers (1-69) and 1 powerball (1-26)
      regular_numbers = sorted(np.random.choice(69, 5, replace=False) + 1)
      powerball = np.random.randint(1, 27)
      
      # Add regular numbers
      for num in regular_numbers:
            features = prepare_powerball_features(num)
            data.append((features, 0))  # 0 for regular numbers
            
      # Add powerball
      features = prepare_powerball_features(powerball)
      data.append((features, 1))  # 1 for powerball
   
   # Convert to numpy arrays
   X = np.array([d[0] for d in data])
   y = np.array([d[1] for d in data])
   
   # Create and train the tree
   tree = PowerballDecisionTree(max_depth=3)
   tree.fit(X, y)
   
   # Make predictions
   predictions = tree.predict(X)
   accuracy = np.mean(predictions == y)
   print(f"Model Accuracy: {accuracy:.2f}")
   
   # Demonstrate prediction for new numbers
   test_numbers = [7, 23, 45, 56, 67, 13]
   print("\nPredictions for sample numbers:")
   for num in test_numbers:
      features = np.array(prepare_powerball_features(num))
      prediction = tree.predict(features.reshape(1, -1))[0]
      print(f"Number {num}: {'Powerball' if prediction == 1 else 'Regular Ball'}")
   
   # Calculate statistics
   total_numbers = len(y)
   powerball_count = np.sum(y == 1)
   regular_count = np.sum(y == 0)
   
   print(f"\nAnalysis of {total_numbers} numbers:")
   print(f"Regular balls: {regular_count}")
   print(f"Powerballs: {powerball_count}")

if __name__ == "__main__":
   main()
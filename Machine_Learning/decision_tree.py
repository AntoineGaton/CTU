"""
Name: Decision Tree Implementation with Gini Impurity
Date: November 10, 2024
Course: CS379
Description:    Implementation of a decision tree classifier using Gini impurity as the splitting criterion.
                The program includes a custom DecisionTree class that can be trained on categorical data
                and make predictions. The implementation includes tree visualization and is tested on
                a simple weather dataset for predicting if conditions are suitable for playing outside.
"""

import numpy as np
from collections import Counter
import pandas as pd
from typing import List, Dict, Tuple, Union
import matplotlib.pyplot as plt

class Node:
    """Represents a node in the decision tree"""
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature  # Feature to split on
        self.threshold = threshold  # Threshold value for the split
        self.left = left  # Left child node
        self.right = right  # Right child node
        self.value = value  # Predicted class (for leaf nodes)

class DecisionTree:
    """Decision Tree Classifier using Gini impurity"""
    
    def __init__(self, max_depth=5, min_samples_split=2):
        self.max_depth = max_depth  # Maximum depth of the tree
        self.min_samples_split = min_samples_split  # Minimum samples required to split
        self.root = None  # Root node of the tree
    
    def _gini_impurity(self, y: np.ndarray) -> float:
        """
        Calculate Gini impurity for a set of labels
        Gini = 1 - Σ(pi²) where pi is the probability of class i
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

# Example usage with weather dataset
if __name__ == "__main__":
    # Create sample weather dataset
    data = {
        'outlook': ['sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'rainy', 'overcast',
                   'sunny', 'sunny', 'rainy', 'sunny', 'overcast', 'overcast', 'rainy'],
        'temperature': [85, 80, 83, 70, 68, 65, 64, 72, 69, 75, 75, 72, 81, 71],
        'humidity': [85, 90, 78, 96, 80, 70, 65, 95, 70, 80, 70, 90, 75, 80],
        'windy': [False, True, False, False, False, True, True, False, False, 
                 False, True, True, False, True],
        'play': ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 
                'yes', 'yes', 'yes', 'yes', 'no']
    }
    
    # Convert to numerical values
    df = pd.DataFrame(data)
    df['outlook'] = pd.Categorical(df['outlook']).codes
    df['windy'] = df['windy'].astype(int)
    
    # Prepare features and target
    X = df[['outlook', 'temperature', 'humidity', 'windy']].values
    y = df['play'].values
    
    # Create and train the decision tree
    tree = DecisionTree(max_depth=3)
    tree.fit(X, y)
    
    # Make predictions
    predictions = tree.predict(X)
    accuracy = np.mean(predictions == y)
    print(f"Accuracy: {accuracy:.2f}")

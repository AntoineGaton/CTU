# THIS CODE IS ME PLAYING AROUND WITH TF-IDF AND GETTING A BETTER UNDERSTANDING
import pandas as pd
import math

# Sample documents
docA = "The cat is black."
docB = "The dog is brown."

# Split documents into words (Bag of Words - BoW)
bowA = docA.split(" ")
bowB = docB.split(" ")

print(bowA)
print("\n----------------------------------\n")
print(bowB)

# Create a set of all unique words in both documents
wordSet = set(bowA).union(set(bowB))
print("\n----------------------------------\n")
print(wordSet)

# Initialize dictionaries to count word occurrences in each document
wordDictA = dict.fromkeys(wordSet, 0)
wordDictB = dict.fromkeys(wordSet, 0)

print("\n----------------------------------\n")
print(wordDictA)
print("\n----------------------------------\n")
print(wordDictB)

# Count the occurrences of each word in document A
for word in bowA:
    wordDictA[word] += 1

# Count the occurrences of each word in document B
for word in bowB:
    wordDictB[word] += 1

print("\n----------------------------------\n")
print(wordDictA)
print("\n----------------------------------\n")
print(wordDictB)
print("\n----------------------------------\n")

# Create a DataFrame to display word counts
data_table = pd.DataFrame([wordDictA, wordDictB])
print(data_table)

# Function to compute Term Frequency (TF)
def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    
    for word, count in wordDict.items():
        tfDict[word] = count / float(bowCount)  # TF calculation: word count / total words in document
    
    return tfDict

# Compute TF for both documents
tfBowA = computeTF(wordDictA, bowA)
tfBowB = computeTF(wordDictB, bowB)

# Function to compute Inverse Document Frequency (IDF)
def computeIDF(docList):
    idfDict = {}
    N = len(docList)
    
    idfDict = dict.fromkeys(docList[0].keys(), 0)
    
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))  # IDF calculation: log(total documents / number of documents with word)
    
    return idfDict

# Compute IDF for the document set
idfs = computeIDF([wordDictA, wordDictB])

# Function to compute TF-IDF
def computeTFIDF(tfBow, idfs):
    tfidf = {}
    
    for word, val in tfBow.items():
        tfidf[word] = val * idfs[word]  # TF-IDF calculation: TF * IDF
    
    return tfidf

# Compute TF-IDF for both documents
tfidfBowA = computeTFIDF(tfBowA, idfs)
tfidfBowB = computeTFIDF(tfBowB, idfs)

print("\n----------------------------------\n")
# Create a DataFrame to display TF-IDF scores
print(pd.DataFrame([tfidfBowA, tfidfBowB]))

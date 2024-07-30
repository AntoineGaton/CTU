# THIS CODE IS ME PLAYING AROUND WITH NLTK AND GETTING A BETTER UNDERSTANDING
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import ne_chunk, pos_tag

# Download necessary NLTK resources
nltk.download('punkt')  # Tokenizer models
nltk.download('averaged_perceptron_tagger')  # Part of speech tagger models
nltk.download('maxent_ne_chunker')  # Named entity chunker models
nltk.download('words')  # Word list for named entity recognition

# Sample text to analyze
text = "Hello world! My name is Antoine. Today I am running a simple test where I use NLTK library to process text."
news_quote = "WASHINGTON (AP) — WikiLeaks founder Julian Assange will plead guilty to a felony charge in a deal with the U.S. Justice Department that will allow him to walk free and resolve a long-running legal saga that spanned multiple continents and centered on the publication of a trove of classified documents."

# Tokenize text into sentences
sentences = sent_tokenize(text)
print(sentences)

print("\n------------------------------\n")

# Tokenize text into words
words = word_tokenize(text)
print(words)

print("\n------------------------------\n")

# Tag parts of speech for each word
print(nltk.pos_tag(words))

print("\n------------------------------\n")

# Function to extract named entities from text
def entities(text):
    return ne_chunk(pos_tag(word_tokenize(text)))

# Extract named entities from the quote
tree = entities(news_quote)

# Print the tree structure of named entities
tree.pprint()

# Display the tree structure graphically (requires GUI)
tree.draw()

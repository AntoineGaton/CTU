# ===========================================
# Name: Antoine Gaton
# Date: November 2, 2024
# Course: CS379
# Description: This code implements a Long Short-Term Memory (LSTM) neural network to generate haiku poetry 
# based on patterns learned from "Alice in Wonderland". The model:
# - Processes text data from Alice in Wonderland for creative input
# - Uses character-level tokenization and syllable counting for haiku structure (5-7-5)
# - Implements a deep LSTM architecture with embedding layer for text understanding
# - Trains on sequences of 50 characters to predict the next character
# - Generates haiku poetry using temperature-based sampling (0.7) for creativity
# - Supports continuous learning through model checkpointing
# - Features rich console output for monitoring training and generation progress
#
# Why LSTM?
# - LSTMs are ideal for sequential data like text due to their ability to maintain long-term dependencies
# - They can remember important patterns while forgetting irrelevant information through their gate mechanisms
# - Unlike simple RNNs, LSTMs avoid the vanishing gradient problem, making them better at learning long sequences
# - The model can capture the writing style and vocabulary patterns from the source text
#
# Distributed Implementation Considerations:
# - Data Parallelism: Training can be distributed across multiple GPUs/machines using tf.distribute
# - Model Parallelism: Large models can split layers across different devices
# - Parameter Server Architecture: Central servers can store model parameters while workers handle computation
# - Asynchronous Training: Multiple workers can train independently and periodically sync parameters
# - Distributed TensorFlow strategies can be implemented for scalability
#
# Implementation Choices:
# - Character-level tokenization provides finer granularity for creative text generation
# - Embedding layer reduces dimensionality and captures character relationships
# - Two-layer LSTM architecture balances complexity and performance
# - Temperature sampling adds controlled randomness for more creative outputs
# - Syllable counting ensures proper haiku structure while maintaining creative freedom
# ===========================================

import os
import numpy as np
import requests
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model # type: ignore
from tensorflow.keras.layers import LSTM, Dense, Embedding # type: ignore
from tensorflow.keras.utils import to_categorical # type: ignore
from tensorflow.keras.preprocessing.text import Tokenizer # type: ignore
from tensorflow.keras.preprocessing.sequence import pad_sequences # type: ignore
from rich import print, box
from rich.console import Console
from rich.progress import track
from rich.table import Table
from rich.panel import Panel
import pickle
import syllables

console = Console()

def load_text_from_url(url):
   """
   Load text data from a given URL.
   
   Parameters:
   - url: URL string to fetch text data from
   
   Returns:
   - text: The fetched text as a single lowercase string
   """
   console.print("[bold green]Fetching text data from URL...[/bold green]")
   try:
      response = requests.get(url, timeout=10)
      response.raise_for_status()
      text = response.text.lower()
      return text
   except requests.exceptions.RequestException as e:
      console.print(f"[bold red]Error fetching text: {e}[/bold red]")
      raise

def preprocess_text(text, sequence_length=40):
   """
   Preprocess text into sequences for LSTM training.
   
   Parameters:
   - text: The input text to preprocess
   - sequence_length: Length of each sequence (default: 40)
   
   Returns:
   - X: Feature sequences for training
   - y: Target labels for training
   - tokenizer: Fitted tokenizer for text conversion
   - total_chars: Total number of unique characters
   """
   if not text or len(text) <= sequence_length:
      raise ValueError("Text is too short for the given sequence length")
   
   console.print("[bold blue]Tokenizing and encoding text data...[/bold blue]")
   tokenizer = Tokenizer(char_level=True)
   tokenizer.fit_on_texts([text])
   total_chars = len(tokenizer.word_index) + 1

   # Create sequences
   sequences = []
   for i in range(0, len(text) - sequence_length):
      sequence = text[i:i + sequence_length + 1]
      sequences.append(sequence)

   # Encode sequences to integers
   encoded_sequences = tokenizer.texts_to_sequences(sequences)
   encoded_sequences = np.array(encoded_sequences)

   # Separate features and labels
   X, y = encoded_sequences[:, :-1], encoded_sequences[:, -1]
   y = to_categorical(y, num_classes=total_chars)

   return X, y, tokenizer, total_chars

def build_lstm_model(input_length, total_chars):
   """
   Build and compile the LSTM model.
   
   Parameters:
   - input_length: Length of input sequences
   - total_chars: Number of unique characters in dataset
   
   Returns:
   - model: Compiled Keras Sequential model
   """
   model = Sequential([
      Embedding(total_chars, 50, input_shape=(input_length,)),
      LSTM(100, return_sequences=True),
      LSTM(100),
      Dense(total_chars, activation='softmax')
   ])
   model.compile(optimizer='adam', loss='categorical_crossentropy')
   model.summary()
   return model

def train_model(model, X, y, epochs=20, batch_size=128):
   """
   Train the LSTM model on preprocessed data.
   
   Parameters:
   - model: The LSTM model to train
   - X: Training features
   - y: Training labels
   - epochs: Number of training epochs (default: 20)
   - batch_size: Batch size for training (default: 128)
   
   Returns:
   - history: Training history object
   """
   console.print("[bold magenta]Starting model training...[/bold magenta]")
   early_stopping = tf.keras.callbacks.EarlyStopping(
      monitor='loss',
      patience=3,
      restore_best_weights=True
   )
   
   history = model.fit(
      X, y,
      epochs=epochs,
      batch_size=batch_size,
      callbacks=[early_stopping],
      validation_split=0.1,  # Use 10% of data for validation
      verbose=1
   )
   console.print("[bold green]Training complete![/bold green]")
   return history

def generate_text(model, tokenizer, seed_text, num_chars, sequence_length, temperature=1.0):
   """
   Generate new text using the trained model.
   
   Parameters:
   - model: Trained LSTM model
   - tokenizer: Fitted tokenizer for text conversion
   - seed_text: Initial text to start generation
   - num_chars: Number of characters to generate
   - sequence_length: Length of input sequences
   - temperature: Randomness of predictions (default: 1.0)
   
   Returns:
   - generated_text: The generated text string
   """
   for _ in track(range(num_chars), description="Generating characters"):
      # Encode the seed text
      encoded = tokenizer.texts_to_sequences([seed_text])[0]
      encoded = pad_sequences([encoded], maxlen=sequence_length, truncating='pre')
      
      # Get predictions
      predictions = model.predict(encoded, verbose=0)[0]
      
      # Apply temperature
      predictions = np.log(predictions) / temperature
      exp_predictions = np.exp(predictions)
      predictions = exp_predictions / np.sum(exp_predictions)
      
      # Get next character index
      next_index = np.random.choice(len(predictions), p=predictions)
      
      # Convert index to character
      next_char = tokenizer.index_word[next_index]  # Fixed this line
      seed_text += next_char

   return seed_text

def save_training_state(model, tokenizer, history, filepath='model_checkpoint'):
   """
   Save model, tokenizer, and training history.
   
   Parameters:
   - model: Trained LSTM model
   - tokenizer: Fitted tokenizer
   - history: Training history
   - filepath: Base path for saving files
   """
   # Create directory if it doesn't exist
   os.makedirs(filepath, exist_ok=True)
   
   # Save the model with .keras extension
   model.save(f'{filepath}/lstm_model.keras')
   
   # Save the tokenizer
   with open(f'{filepath}/tokenizer.pkl', 'wb') as f:
      pickle.dump(tokenizer, f)
   
   # Save the history
   with open(f'{filepath}/history.pkl', 'wb') as f:
      pickle.dump(history.history, f)
   
   console.print("[bold green]Training state saved successfully![/bold green]")

def load_training_state(filepath='model_checkpoint'):
   """
   Load saved model, tokenizer, and history.
   
   Parameters:
   - filepath: Base path where files are saved
   
   Returns:
   - model: Loaded model
   - tokenizer: Loaded tokenizer
   - history: Loaded history
   """
   try:
      # Load the model with .keras extension
      model = load_model(f'{filepath}/lstm_model.keras')
      
      # Load the tokenizer
      with open(f'{filepath}/tokenizer.pkl', 'rb') as f:
         tokenizer = pickle.load(f)
      
      # Load the history
      with open(f'{filepath}/history.pkl', 'rb') as f:
         history = pickle.load(f)
      
      return model, tokenizer, history
   except Exception as e:
      console.print(f"[bold red]Error loading training state: {e}[/bold red]")
      return None, None, None

def display_config(config):
   """Display configuration parameters in a formatted panel"""
   config_table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
   config_table.add_column("Parameter", style="cyan")
   config_table.add_column("Value", style="green")
   
   for key, value in config.items():
      config_table.add_row(str(key), str(value))
   
   return Panel(config_table, title="[bold blue]Configuration", border_style="blue")

def display_model_summary(model):
   """Capture and display model summary in a formatted panel"""
   # Redirect model summary to string
   from io import StringIO
   import sys
   old_stdout = sys.stdout
   string_buffer = StringIO()
   sys.stdout = string_buffer
   model.summary()
   sys.stdout = old_stdout
   
   return Panel(string_buffer.getvalue(), title="[bold blue]Model Architecture", border_style="blue")

def count_syllables(word):
   """
   Count syllables in a word using the syllables library.
   
   Parameters:
   - word: String to count syllables in
   
   Returns:
   - count: Number of syllables
   """
   try:
      return syllables.estimate(word)
   except:
      # Fallback if word not found
      return len(word.split('-'))

def generate_haiku(model, tokenizer, temperature=0.7):
   """
   Generate a haiku (5-7-5 syllable pattern) using syllables library for accuracy.
   
   Parameters:
   - model: Trained LSTM model
   - tokenizer: Fitted tokenizer
   - temperature: Controls randomness of generation (default: 0.7)
   
   Returns:
   - haiku: Generated haiku as string with line breaks
   """
   def generate_line(target_syllables):
      line = ""
      syllable_count = 0
      attempts = 0
      max_attempts = 50  # Prevent infinite loops
      
      while syllable_count < target_syllables and attempts < max_attempts:
         seed = line if line else "wonderland dreams"
         next_words = generate_text(
               model, tokenizer, seed,
               num_chars=30,  # Generate more text for better word choices
               sequence_length=CONFIG['sequence_length'],
               temperature=temperature
         )
         
         words = next_words.split()
         for word in words:
               word_syllables = count_syllables(word)
               if syllable_count + word_syllables <= target_syllables:
                  line += word + " "
                  syllable_count += word_syllables
               if syllable_count == target_syllables:
                  break
         attempts += 1
      
      return line.strip()
   
   # Generate each line with proper syllable counts
   line1 = generate_line(5)  # First line: 5 syllables
   line2 = generate_line(7)  # Second line: 7 syllables
   line3 = generate_line(5)  # Third line: 5 syllables
   
   return f"{line1}\n{line2}\n{line3}"

if __name__ == "__main__":
   CONFIG = {
      'url': "https://gist.githubusercontent.com/phillipj/4944029/raw/75ba2243dd5ec2875f629bf5d79f6c1e4b5a8b46/alice_in_wonderland.txt",
      'sequence_length': 50,
      'epochs': 25,
      'batch_size': 128,
      'seed_text': "Down the rabbit-hole she went, following the White Rabbit, never once considering how in the world she was to get out again.",
      'num_chars_to_generate': 250,
      'temperature': 0.7,
      'continue_training': True
   }
   
   try:
      # Create section divider function for cleaner code
      def create_section_panel(title, content):
         """Creates a panel with title and content in the style of Configuration section"""
         return Panel(
               content,
               title=f"[bold blue]{title}[/bold blue]",
               border_style="blue",
               padding=(1, 2)
         )

      # Display configuration
      console.print(display_config(CONFIG))
      
      # Data Loading Section
      with console.status("[bold blue]Loading and preprocessing data...") as status:
         text = load_text_from_url(CONFIG['url'])
         status.update("[bold blue]Preprocessing text...")
         X, y, tokenizer, total_chars = preprocess_text(text, CONFIG['sequence_length'])
         loading_content = "[green]✓ Data loaded and preprocessed successfully[/green]"
         console.print(create_section_panel("Data Loading", loading_content))
      
      # Model Section
      if CONFIG['continue_training']:
         model, saved_tokenizer, prev_history = load_training_state()
         if model is None:
               model_status = "[yellow]No previous model found. Starting fresh training...[/yellow]"
               model = build_lstm_model(CONFIG['sequence_length'], total_chars)
         else:
               model_status = "[green]Loaded previous model successfully![/green]"
               tokenizer = saved_tokenizer
      else:
         model = build_lstm_model(CONFIG['sequence_length'], total_chars)
         model_status = "[blue]Created new model[/blue]"
      
      console.print(create_section_panel("Model Status", model_status))
      console.print(display_model_summary(model))
      
      # Training Section
      history = train_model(model, X, y, CONFIG['epochs'], CONFIG['batch_size'])
      save_training_state(model, tokenizer, history)
      training_content = "[green]✓ Model trained and saved successfully[/green]"
      console.print(create_section_panel("Training Progress", training_content))
      
      # Regular Text Generation Section
      console.print(create_section_panel("Text Generation", "[bold]Generating story continuation...[/bold]"))
      generated_text = generate_text(
         model, tokenizer, CONFIG['seed_text'],
         CONFIG['num_chars_to_generate'],
         CONFIG['sequence_length'],
         CONFIG['temperature']
      )
      console.print(create_section_panel(
         "Generated Story",
         f"[green]{generated_text}[/green]"
      ))
      
      # Haiku Generation Section
      console.print(create_section_panel("Haiku Generation", "[bold]Generating haiku...[/bold]"))
      haiku = generate_haiku(model, tokenizer, CONFIG['temperature'])
      console.print(create_section_panel(
         "Generated Haiku",
         f"[bold green]\n"
         f"{haiku.split('\n')[0]:<14}\n"
         f"{haiku.split('\n')[1]:<14}\n"
         f"{haiku.split('\n')[2]:<14}\n"
         f"[/bold green]"
      ))
      
   except Exception as e:
      console.print(create_section_panel(
         "Error",
         f"[bold red]An error occurred: {str(e)}[/bold red]"
      ))

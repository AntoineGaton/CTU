import pandas as pd

# Load the CSV file
# csv_data = pd.read_csv('../NoSQL/sidewalk-cafe-permits.csv')
csv_data = pd.read_csv('../NoSQL/catalog.csv')

# Convert the dataframe to JSON
# json_data = df.to_json(orient='records')

# Convert only the first 5 records to JSON
json_data = csv_data.head(5).to_json(orient='records')

# Save the JSON to a file
with open('data2.json', 'w') as file:
    file.write(json_data)

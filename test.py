import pymongo
from sensor.constants.database import COLLECTION_NAME, DATABASE_NAME
import pandas as pd
import sys,os

# Replace 'your_mongodb_uri' with your actual MongoDB connection URI
URL= os.getenv("MONGO_DB_URL",None)
client = pymongo.MongoClient(URL)

db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]
chunk_size = 1000
# Fetch all documents from the collection
total=1000
current_position = 0
all_data = []
# Loop through the collection in chunks
while current_position < total:
    # Fetch a chunk of documents
    data = list(collection.find().skip(current_position).limit(chunk_size))
    all_data.extend(data)

    # Process the chunk (you can modify this part according to your needs)
    for document in data:
        print(document)

    # Update the current position
    current_position += chunk_size

df = pd.DataFrame(all_data)
print(df.iloc[:,1])
# Write the DataFrame to a CSV file
df.to_csv("data_from_mongodb.csv", index=False)


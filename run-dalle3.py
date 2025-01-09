from openai import AzureOpenAI
from PIL import Image
import requests
import json
import os
import csv

# Extracting environment variables
AOAI_API_BASE = ""
AOAI_API_KEY = ""
AOAI_API_VERSION = "2024-02-01"
AOAI_DEPLOYMENT = "dall-e-3"  # Replace with your deployment name

# Instantiate Azure OpenAI client
client = AzureOpenAI(
    api_version=AOAI_API_VERSION,
    api_key=AOAI_API_KEY,
    azure_endpoint=AOAI_API_BASE,
)

# Helper function
def image_generator(prompt, round_label, name):
    try:
        # Generate image with DALL-E 3
        response = client.images.generate(
            model=AOAI_DEPLOYMENT,
            prompt=prompt,
        )
        
        # Print and inspect the response structure
        print(json.dumps(response.model_dump_json(), indent=2))
        
        # Extract image URL
        json_response = json.loads(response.model_dump_json())
        image_url = json_response["data"][0]["url"]  # Ensure this key path matches the response

        # Set the directory for the stored image
        image_dir = os.path.join(os.curdir, round_label)
        if not os.path.isdir(image_dir):
            os.makedirs(image_dir)  # Create directories if they don't exist

        # Initialize the image path
        image_name = f"{name}.png"
        image_path = os.path.join(image_dir, image_name)

        # Retrieve and save the generated image
        response = requests.get(image_url)
        response.raise_for_status()  # Raise HTTP errors if any
        with open(image_path, "wb") as image_file:
            image_file.write(response.content)
        
        return image_url
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Path to your CSV file
csv_file = 'myPromo.csv'

# Open the CSV file and read the data
with open(csv_file, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    # Skip the header if your CSV has one
    next(reader, None)  # Uncomment this if there is a header row
    i = 42
    labels = ['A', 'B', 'C', 'D', 'E']
    # Iterate over each row
    for row in reader:
        for label in labels:
            name = f"DallE{label}{i}"  # Create unique image name
            prompt = row[0]  # Assuming column 0 contains the prompt
            # Call the function with values from the row
            image_generator(prompt, label, name)
        i += 1

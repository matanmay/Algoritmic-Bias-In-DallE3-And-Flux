import csv
from pathlib import Path
from pydantic import BaseModel
from typing import Literal
from ollama import chat

# Define the schema for image objects
class Object(BaseModel):
    name: str
    confidence: float
    attributes: str

class Person(BaseModel):
    age: int
    gender: str
    ethnicity: str  # Use lowercase for consistency with CSV keys
    skin_color: str  # Use snake_case for consistency (PEP 8)

class ImageDescription(BaseModel):
    person1: Person
    person2: Person

def describe_images(path):
    # Verify the file exists
    if not path.exists():
        raise FileNotFoundError(f'Image not found at: {path}')

    # Set up chat as usual
    response = chat(
        model='llama3.2-vision',
        format=ImageDescription.model_json_schema(),  # Pass in the schema for the response
        messages=[
            {
                'role': 'user',
                'content': 'Analyze this image and return a detailed JSON description including objects, scene, colors and any text detected. If you cannot determine certain details, leave those fields empty.',
                'images': [path],
            },
        ],
        options={'temperature': 0},  # Set temperature to 0 for more deterministic output
    )

    # Convert received content to the schema
    return ImageDescription.model_validate_json(response.message.content)

# Initialize the CSV file and write the header
output_file = "image_descriptions.csv"
fieldnames = [
    'path', 'le', 'i',
    'person1-age', 'person1-gender', 'person1-ethnicity', 'person1-skin-color',
    'person2-age', 'person2-gender', 'person2-ethnicity', 'person2-skin-color'
]

# **Explicitly Open, Write, and Close the File for Each Operation**
# This is not the most efficient way but helps in debugging. Normally, you'd keep the file open for all writes.
with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csv_writer.writeheader()
    print("Header written successfully.")

l = ['A', 'B', 'C', 'D', 'E']
for le in l:
    for i in range(1, 62):
        path = Path(f'{le}/Flux{le}{i}.png')
        try:
            description = describe_images(path)
            row = {
                'path': str(path),
                'le': le,
                'i': i,
                'person1-age': description.person1.age,
                'person1-gender': description.person1.gender,
                'person1-ethnicity': description.person1.ethnicity,
                'person1-skin-color': description.person1.skin_color,
                'person2-age': description.person2.age,
                'person2-gender': description.person2.gender,
                'person2-ethnicity': description.person2.ethnicity,
                'person2-skin-color': description.person2.skin_color
            }
            print("Attempting to write row:", row)
            with open(output_file, mode='a', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                try:
                    csv_writer.writerow(row)
                    print("Row written successfully to CSV.")
                except Exception as e:
                    print(f"Error writing to CSV for {path}: {e}")
        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(f"Error processing {path}: {e}")

print(f"Descriptions processing completed. Check {output_file} for outputs.")

import os
import csv
import json
import pandas as pd
from PIL import Image
import PyPDF2

def list_files(directory):
    """List all files in the dataset directory."""
    files = os.listdir(directory)
    print("Files in dataset:")
    for file in files:
        print(file)
    return files

def read_text_file(file_path):
    """Read and print the first 5 lines of a text file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for _ in range(5):
                print(file.readline().strip())
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

def read_csv_file(file_path):
    """Read and display the first 3 rows of a CSV file."""
    try:
        df = pd.read_csv(file_path)
        print(df.head(3))
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

def read_json_file(file_path):
    """Parse and display key-value pairs from a JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            print(json.dumps(data, indent=4)[:500])  # Print first 500 chars
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

def read_excel_file(file_path):
    """Read and display the first 3 rows of an Excel file."""
    try:
        df = pd.read_excel(file_path)
        print(df.head(3))
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

def open_image_file(file_path):
    """Open and display an image file."""
    try:
        img = Image.open(file_path)
        img.show()
    except Exception as e:
        print(f"Error opening {file_path}: {e}")

def read_pdf_file(file_path):
    """Extract and print text from the first few lines of a PDF file."""
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages[:2]:
                print(page.extract_text())
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

# Main Execution
dataset_directory = "dataset"
files = list_files(dataset_directory)

for file in files:
    file_path = os.path.join(dataset_directory, file)
    if file.endswith(".txt"):
        read_text_file(file_path)
    elif file.endswith(".csv"):
        read_csv_file(file_path)
    elif file.endswith(".json"):
        read_json_file(file_path)
    elif file.endswith(".xlsx"):
        read_excel_file(file_path)
    elif file.endswith(".jpg") or file.endswith(".png"):
        open_image_file(file_path)
    elif file.endswith(".pdf"):
        read_pdf_file(file_path)

import os
import csv
import requests

def download_csv(url, filename):
    """Download CSV file from the given URL and save it locally."""
    response = requests.get(url)
    with open(filename, "wb") as file:
        file.write(response.content)
    print(f"Downloaded CSV: {filename}")

def read_csv(filename):
    """Read CSV file and return its content as a list of rows."""
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        return list(reader)

def download_flags(csv_file):
    """Extract flag URLs from CSV and download them into 'flags' directory."""
    if not os.path.exists("flags"):
        os.makedirs("flags")
    
    data = read_csv(csv_file)
    headers = data[0]
    country_index = headers.index("country")
    flag_url_index = headers.index("flag")
    
    for row in data[1:]:
        country = row[country_index]
        flag_url = row[flag_url_index]
        flag_filename = os.path.join("flags", f"{country}.png")
        
        response = requests.get(flag_url)
        with open(flag_filename, "wb") as file:
            file.write(response.content)
        print(f"Downloaded flag: {flag_filename}")

# Main script execution
flags_csv_url = "https://raw.githubusercontent.com/prasertcbs/basic-dataset/refs/heads/master/Country_Flags.csv"
flags_csv_filename = "country_flags.csv"
download_csv(flags_csv_url, flags_csv_filename)
download_flags(flags_csv_filename)

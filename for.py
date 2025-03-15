import requests

# Function to download the CSV file
def download_csv(url, filename):
    """Downloads a CSV file from the given URL and saves it locally."""
    response = requests.get(url)
    with open(filename, "wb") as file:
        file.write(response.content)
    print(f"Downloaded CSV: {filename}")

# Function to count Nobel Prizes by country
def count_nobel_prizes(csv_file):
    """Reads the CSV file, extracts birth country data, and counts the Nobel Prizes per country."""
    with open(csv_file, "r", encoding="utf-8") as file:
        lines = file.read().splitlines()
    
    headers = lines[0].split(",")
    country_index = headers.index("birth_country")
    
    country_counts = []  # List to store the count of Nobel Prizes per country
    country_names = []   # List to store unique country names
    
    for line in lines[1:]:
        fields = line.split(",")
        country = fields[country_index]
        
        if country in country_names:
            index = country_names.index(country)
            country_counts[index] += 1
        else:
            country_names.append(country)
            country_counts.append(1)
    
    return country_names, country_counts

# Function to sort countries by Nobel Prize count
def sort_countries(country_names, country_counts):
    """Sorts the countries based on Nobel Prize count using Bubble Sort."""
    for i in range(len(country_counts)):
        for j in range(i + 1, len(country_counts)):
            if country_counts[j] > country_counts[i]:
                country_counts[i], country_counts[j] = country_counts[j], country_counts[i]
                country_names[i], country_names[j] = country_names[j], country_names[i]
    
    return country_names[:20], country_counts[:20]

# Main execution
nobel_csv_url = "https://raw.githubusercontent.com/prasertcbs/basic-dataset/refs/heads/master/Nobel%20Laureattes.csv"
nobel_csv_filename = "nobel_laureates.csv"
download_csv(nobel_csv_url, nobel_csv_filename)

# Count Nobel Prizes by country
countries, counts = count_nobel_prizes(nobel_csv_filename)

# Get top 20 countries
top_countries, top_counts = sort_countries(countries, counts)

# Print results
print("Top 20 Countries with Most Nobel Prizes:")
for i in range(len(top_countries)):
    print(f"{top_countries[i]}: {top_counts[i]}")

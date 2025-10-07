import requests
from bs4 import BeautifulSoup
import os

# Define the base URL
URL = "https://www.kaggle.com"

# Make an HTTP GET request
response = requests.get(URL)
print("response -->", response, "\ntype -->", type(response))
print("text -->", response.text, "\ncontent -->", response.content, "\nstatus_code -->", response.status_code)

if response.status_code != 200:
    print("HTTP connection is not successful! Try again.")
else:
    print("HTTP connection is successful!")

# Parse the content with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
print("title with tags -->", soup.title)
print("title without tags -->", soup.title.text)

# Print all "link" tags
for link in soup.find_all("link"):
    print(link.get("href"))

# Print all text content
print(soup.get_text())

# Create a folder to save HTML files
folder = "mini_dataset"
if not os.path.exists(folder):
    os.mkdir(folder)

# Function to scrape content
def scrape_content(URL):
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            print("HTTP connection is successful for the URL:", URL)
            return response
        else:
            print("HTTP connection failed for the URL:", URL)
            return None
    except Exception as e:
        print(f"An error occurred while fetching {URL}: {e}")
        return None

# Function to save HTML content to a file
def save_html(to_where, text, name):
    file_name = name + ".html"
    file_path = os.path.join(to_where, file_name)
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)
    except Exception as e:
        print(f"An error occurred while saving {file_name}: {e}")

# Test save_html function
test_text = response.text
save_html(folder, test_text, "example")

# List of URLs to scrape
URL_list = [
    "https://www.kaggle.com",
    "https://stackoverflow.com",
    "https://www.easyhindityping.com/english-to-hindi-translation",
    "https://testbook.com/",
    "https://www.britannica.com/money",
    "https://www.youtube.com/",
    "https://github.com/",
    "https://www.cuh.ac.in/",
    "https://www.linkedin.com/home?originalSubdomain=in",
    "https://ecomexpress.in/",
]

# Function to create a mini dataset
def create_mini_dataset(to_where, URL_list):
    for i, url in enumerate(URL_list):
        content = scrape_content(url)
        if content:
            save_html(to_where, content.text, str(i))
    print("Mini dataset is created!")

# Run the dataset creation
create_mini_dataset(folder, URL_list)

# Check if you have 10 different HTML files

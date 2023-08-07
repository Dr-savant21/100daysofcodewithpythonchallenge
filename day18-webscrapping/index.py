import requests
from bs4 import BeautifulSoup

# Send a GET request to the BBC News homepage
response = requests.get("https://www.bbc.com/news")

# Create a BeautifulSoup object with the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the news headlines on the page
headlines = soup.find_all("a", class_="gs-c-promo-heading")

# Extract and print the text of each headline
for headline in headlines:
    print(headline.get_text(strip=True))

import requests
from bs4 import BeautifulSoup

def get_zillow_stats(location):
    base_url = f'https://www.zillow.com/homes/{location}_rb/'

    # Send an HTTP request to the URL
    response = requests.get(base_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting relevant information (customize according to Zillow's structure)
        price = soup.find('div', class_='home-summary-row').find('span', class_='ds-value').text.strip()
        address = soup.find('header', class_='ds-home-details-chip').find('h1').text.strip()

        print(f"Location: {address}")
        print(f"Price: {price}")
    else:
        print(f"Error: Unable to fetch data for {location}")

if __name__ == "__main__":
    location_input = input("Enter the location (e.g., city-state-zip): ")
    get_zillow_stats(location_input)

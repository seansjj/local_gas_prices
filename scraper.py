import pandas as pd
import requests

from bs4 import BeautifulSoup
from datetime import datetime

# function to scrape gas prices
def scrape_gas_prices(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # find the table with the gas prices
    price_element = soup.find('div', class_='price')
    price = price_element.text if price_element else 'N/A'

    return price

# log prices at specific times
def log_prices(url):
    # scrape current price
    price = scrape_gas_prices(url)
    now = datetime.now()

    # add data to csv
    with open('gas_prices.csv', 'a') as f:
        f.write(f'{now},{price}\n')

# gasbuddy url
url = 'https://www.gasbuddy.com/station/69982'

# log manually
log_prices(url)

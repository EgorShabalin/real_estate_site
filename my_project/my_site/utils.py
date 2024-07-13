import requests
import xml.etree.ElementTree as ET

"""
def get_exchange_rates():
    # URL for the Central Bank of Turkey's exchange rates
    url = "https://www.tcmb.gov.tr/kurlar/today.xml"

    # Fetch the XML data
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the XML
        root = ET.fromstring(response.content)

        # Dictionary to store our results
        rates = {}

        # Iterate through the currency elements
        for currency in root.findall("Currency"):
            code = currency.get("CurrencyCode")
            name = currency.find("CurrencyName").text
            forex_buying = currency.find("ForexBuying").text
            forex_selling = currency.find("ForexSelling").text

            rates[code] = {
                "name": name,
                "forex_buying": forex_buying,
                "forex_selling": forex_selling,
            }

        return rates
    else:
        print(f"Failed to fetch data: HTTP {response.status_code}")
        return None


n = 1.005


def get_prices(price):
    price = price.replace(" ", "")
    price = float(price)
    rates = get_exchange_rates()
    for k, v in rates.items():
        if k == "USD":
            usd_sell = v["forex_selling"]
        if k == "EUR":
            eur_sell = v["forex_selling"]
        if k == "RUB":
            rub_sell = v["forex_selling"]

    usd_price = (price / float(usd_sell)) * n
    eur_price = (price / float(eur_sell)) * n
    rub_price = (price / float(rub_sell)) * n

    return [int(usd_price), int(eur_price), int(rub_price)]
"""

import os
import time
import requests
import xml.etree.ElementTree as ET
from datetime import datetime


def get_exchange_rates():
    # URL of the XML data
    url = "https://www.tcmb.gov.tr/kurlar/today.xml"

    # Number of retries
    max_retries = 3
    success = False

    # File name to save XML data
    file_name = "today.xml"

    # Check if the file exists and is from today
    def is_file_from_today(file_path):
        if os.path.exists(file_path):
            file_time = os.path.getmtime(file_path)
            file_date = datetime.fromtimestamp(file_time).date()
            if file_date == datetime.today().date():
                return True
        return False

    # Function to fetch and save data
    def fetch_and_save_data():
        nonlocal success
        for attempt in range(max_retries):
            try:
                # Fetch the XML data
                response = requests.get(url)
                response.raise_for_status()  # Raise an exception for HTTP errors

                # Save the XML data to a file
                with open(file_name, "wb") as file:
                    file.write(response.content)

                print(f"Data has been fetched and saved to {file_name}")
                success = True
                break  # Exit the loop on success

            except (requests.exceptions.RequestException, ET.ParseError) as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(1)  # Wait for a second before retrying

    # Function to parse XML content and extract exchange rates
    def parse_exchange_rates(xml_content):
        root = ET.fromstring(xml_content)

        # Dictionary to store our results
        rates = {}

        # Iterate through the currency elements
        for currency in root.findall("Currency"):
            code = currency.get("CurrencyCode")
            name = currency.find("CurrencyName").text
            forex_buying = currency.find("ForexBuying").text
            forex_selling = currency.find("ForexSelling").text

            rates[code] = {
                "name": name,
                "forex_buying": forex_buying,
                "forex_selling": forex_selling,
            }

        return rates

    # Main function logic
    # Check if the file is from today
    if not is_file_from_today(file_name):
        # Fetch and save data if the file is not from today
        fetch_and_save_data()

    # Read and parse the XML content
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            xml_content = file.read()

        # Parse exchange rates
        rates = parse_exchange_rates(xml_content)

        # Print the extracted exchange rates
        # for code, data in rates.items():
        #    print(f"Currency: {data['name']} ({code})")
        #    print(f"  Forex Buying: {data['forex_buying']}")
        #    print(f"  Forex Selling: {data['forex_selling']}")

        return rates
    else:
        print(
            "Failed to fetch data after several attempts or no data available from today."
        )
        return None


n = 1.005


def get_usd(price):
    try:
        price = price.replace(" ", "")
        price = float(price)
        rates = get_exchange_rates()
        for k, v in rates.items():
            if k == "USD":
                rate = v["forex_selling"]

        usd_price = (price / float(rate)) * n
    except:
        usd_price = 0

    return int(usd_price)


def get_eur(price):
    try:
        price = price.replace(" ", "")
        price = float(price)
        rates = get_exchange_rates()
        for k, v in rates.items():
            if k == "EUR":
                rate = v["forex_selling"]

        eur_price = (price / float(rate)) * n
    except:
        eur_price = 0

    return int(eur_price)


def get_rub(price):
    try:
        price = price.replace(" ", "")
        price = float(price)
        rates = get_exchange_rates()
        for k, v in rates.items():
            if k == "RUB":
                rate = v["forex_selling"]

        rub_price = (price / float(rate)) * n
    except:
        rub_price = 0

    return int(rub_price)

import requests
import xml.etree.ElementTree as ET


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

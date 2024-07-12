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

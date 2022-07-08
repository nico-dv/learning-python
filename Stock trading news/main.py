import requests
import os
from dotenv import load_dotenv
 

def configure():
    load_dotenv()

configure()


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey":os.getenv('stock_key')

}


response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

daybefore_yesterday_data = data_list[1]
daybefore_yesterday_closing_price = daybefore_yesterday_data["4. close"]

difference = abs(float(yesterday_closing_price)) - abs(float(daybefore_yesterday_closing_price))

diff_percent = (difference / float(yesterday_closing_price)) * 100

print(diff_percent)

if diff_percent > 5:
    print("The variation is greater than 5%.")

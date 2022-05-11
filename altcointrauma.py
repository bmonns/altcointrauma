from urllib import request
import requests

price_url = 'https://api.coingecko.com/api/v3/coins/zookeeper?localization=false&tickers=false&market_data=true'
response = requests.get(price_url)
current_price = response.json()['market_data']['current_price']['usd']

url = 'https://maker.ifttt.com/trigger/test_event/with/key/cu-0QxWSdbV5uQRZTdr8Ol'
data = {
    "value1":current_price
    }
requests.post(url, json=data)


from locale import getpreferredencoding
from pickle import TRUE
from time import time
from urllib import request
import time
import requests

def getprice_postifttt():

    while TRUE:
        price_url = 'https://api.coingecko.com/api/v3/coins/zookeeper?localization=false&tickers=false&market_data=true'
        response = requests.get(price_url)

        #currency prices
        current_usd = response.json()['market_data']['current_price']['usd']
        current_rub = response.json()['market_data']['current_price']['rub']

        ifttt_url = 'https://maker.ifttt.com/trigger/test_event/with/key/cu-0QxWSdbV5uQRZTdr8Ol'
        data = {
            "value1":current_usd,
            "value2":current_rub
            }
        requests.post(ifttt_url, json=data)
        print('Post Completed')
        time.sleep(21600)

getprice_postifttt()











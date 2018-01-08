#!/usr/bin/python

import requests
import json
import time

SECRET_KEY = 'xxxx'

def usdtCnyMonitor():

    r = requests.get('https://gate.io/json_svr/query_push/?u=13&c=506680&type=push_main_rates&symbol=USDT_CNY')
    print(r.text)
    data = json.loads(r.text)
    # {"result":true,"appraised_rates":{"buy_rate":"7.36","sell_rate":"7.31","max_rate":"7.90","min_rate":"6.59","rate_24h_ago":"7.21"}}
    result = data.get('result')
    if result:
        rates = data.get('appraised_rates')
        buyRate = rates.get('buy_rate')
        print ('rate:' + buyRate)
        if (float(buyRate) <= 7.0 or float(buyRate) >= 7.7):
            requests.post('https://sc.ftqq.com/' + SECRET_KEY + '.send?text=monitor&desp=rate:' + buyRate) 

if __name__ == '__main__':
    while (True):
        usdtCnyMonitor()
        time.sleep(60)

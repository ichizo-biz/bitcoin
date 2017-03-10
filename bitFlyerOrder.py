# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 12:14:31 2017

@author: ichizo
"""

import ApiCall

api_key = 'APIキー'
api_secret = 'APIシークレット'
api_endpoint = 'https://api.bitflyer.jp'

path = '/v1/board?product_code=BTC_JPY'
order_path = '/v1/me/sendchildorder'
body = {
  "product_code": "BTC_JPY",
  "child_order_type": "LIMIT",
  "side": "SELL",
  "price": 300000,
  "size": 0.001,
  "minute_to_expire": 10000,
  "time_in_force": "GTC"
}


if __name__ == '__main__':
    api = ApiCall.ApiCall(api_key,api_secret,api_endpoint)
    result = api.get_api_call(path).json()
    print(result)
    
    result = api.post_api_call(order_path,body).json()
    print(result)

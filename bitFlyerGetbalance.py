# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 12:14:31 2017

@author: ichizo
"""

import ApiCall

api_key = 'APIキー'
api_secret = 'APIシークレット'
api_endpoint = 'https://api.bitflyer.jp'

path = '/v1/me/getbalance'


if __name__ == '__main__':
    api = ApiCall.ApiCall(api_key,api_secret,api_endpoint)
    result = api.get_api_call(path).json()
    print(result)

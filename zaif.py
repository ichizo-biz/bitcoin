# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 14:37:22 2017

@author: ichizo
"""

from zaifapi import ZaifPublicApi, ZaifPrivateApi

api_key = 'APIキー'
api_secret = 'APIシークレット'

zaif = ZaifPublicApi()
print(zaif.depth('btc_jpy'))
"""
zaif = ZaifPrivateApi(api_key, api_secret)
print(zaif.get_info())
"""
zaif = ZaifPrivateApi(api_key, api_secret)
print(zaif.trade(currency_pair="btc_jpy",action="bid",price=5000,amount=0.001))

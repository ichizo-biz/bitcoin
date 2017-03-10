# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 12:00:27 2017

@author: ichizo
"""

import json
import requests
import time
import hmac
import hashlib

class ApiCall:
    def __init__(self,api_key,api_secret,api_endpoint):
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_endpoint = api_endpoint
        
    def get_api_call(self,path):
        method = 'GET'
        timestamp = str(time.time())
        text = timestamp + method + path
        sign = hmac.new(bytes(self.api_secret.encode('ascii')), bytes(text.encode('ascii')), hashlib.sha256).hexdigest()
        request_data=requests.get(
            self.api_endpoint+path
            ,headers = {
                'ACCESS-KEY': self.api_key,
                'ACCESS-TIMESTAMP': timestamp,
                'ACCESS-SIGN': sign,
                'Content-Type': 'application/json'
            })
        return request_data
    
    
    def post_api_call(self,path,body):
        body = json.dumps(body)
        method = 'POST'
        timestamp = str(time.time())
        text = timestamp + method + path + body
        sign = hmac.new(bytes(self.api_secret.encode('ascii')), bytes(text.encode('ascii')), hashlib.sha256).hexdigest()
        request_data=requests.post(
            self.api_endpoint+path
            ,data= body
            ,headers = {
                'ACCESS-KEY': self.api_key,
                'ACCESS-TIMESTAMP': timestamp,
                'ACCESS-SIGN': sign,
                'Content-Type': 'application/json'
            })
        return request_data

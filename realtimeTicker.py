# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:24:33 2017

@author: ichizo
"""
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub, SubscribeListener
import sqlite3
import time
import datetime

DB = 'bitflyer.db'


if __name__ == '__main__':

    pnconfig = PNConfiguration()
    pnconfig.subscribe_key = "sub-c-52a9ab50-291b-11e5-baaa-0619f8945a4f"
    pnconfig.ssl = False
     
    pubnub = PubNub(pnconfig)
    
    my_listener = SubscribeListener()
    pubnub.add_listener(my_listener)
     
    pubnub.subscribe().channels(['lightning_ticker_BTC_JPY', 'lightning_ticker_FX_BTC_JPY']).execute()
    my_listener.wait_for_connect()
    print('connected')
    
    i = 0
    while i < 360:
        
        conn = sqlite3.connect(DB)
        cur = conn.cursor()

        result = my_listener.wait_for_message_on('lightning_ticker_BTC_JPY')
        print(result.message)
        bc_data = result.message
        print(bc_data['best_bid'])
        
        fx_result = my_listener.wait_for_message_on('lightning_ticker_FX_BTC_JPY')
        print(fx_result.message)
        fx_data = fx_result.message
        print(fx_data['best_bid'])

        sql = "INSERT INTO btcfx (bc_total_bid_depth, bc_total_ask_depth, bc_ltp, \
            bc_tick_id, bc_volume, bc_best_bid, bc_best_ask_size, \
            bc_volume_by_product, bc_product_code, bc_timestamp, \
            bc_best_bid_size, bc_best_ask, \
            fx_total_bid_depth, fx_total_ask_depth, fx_ltp, \
            fx_tick_id, fx_volume, fx_best_bid, fx_best_ask_size, \
            fx_volume_by_product, fx_product_code, fx_timestamp, \
            fx_best_bid_size, fx_best_ask, \
            diff_bid, diff_ask, created) \
            VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',\
            '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',\
            '%s','%s','%s','%s','%s','%s','%s')" \
            % (bc_data['total_bid_depth'], bc_data['total_ask_depth'], bc_data['ltp'], \
            bc_data['tick_id'], bc_data['volume'], bc_data['best_bid'], bc_data['best_ask_size'], \
            bc_data['volume_by_product'], bc_data['product_code'], bc_data['timestamp'], \
            bc_data['best_bid_size'], bc_data['best_ask'], \
            fx_data['total_bid_depth'], fx_data['total_ask_depth'], fx_data['ltp'], \
            fx_data['tick_id'], fx_data['volume'], fx_data['best_bid'], fx_data['best_ask_size'], \
            fx_data['volume_by_product'], fx_data['product_code'], fx_data['timestamp'], \
            fx_data['best_bid_size'], fx_data['best_ask'], \
            bc_data['best_bid'] - fx_data['best_bid'], bc_data['best_ask'] - fx_data['best_ask'], datetime.datetime.now())

        print(sql)
        cur.execute(sql)
        conn.commit()
        conn.close()
        i = i + 1
        
        time.sleep(60)

    pubnub.unsubscribe().channels(['lightning_ticker_BTC_JPY', 'lightning_ticker_FX_BTC_JPY']).execute()
    my_listener.wait_for_disconnect()
    
    print('unsubscribed')


 


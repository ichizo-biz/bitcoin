# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:24:33 2017

@author: ichizo
"""
import requests
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub, SubscribeListener
import pymysql
import datetime

dbh = pymysql.connect(
         host='localhost',
         user='root',
         password='',
         db='bitcoin',
         charset='utf8',
         cursorclass=pymysql.cursors.DictCursor
    )

COINCHECK = 'https://coincheck.com/api/ticker'
QUOINE = 'https://api.quoine.com/products/5'
ZAIF = 'https://api.zaif.jp/api/1/ticker/btc_jpy'
BTCBOX = 'https://www.btcbox.co.jp/api/v1/ticker/'

if __name__ == '__main__':

    pnconfig = PNConfiguration()
    pnconfig.subscribe_key = "sub-c-52a9ab50-291b-11e5-baaa-0619f8945a4f"
    pnconfig.ssl = False
     
    pubnub = PubNub(pnconfig)
    
    my_listener = SubscribeListener()
    pubnub.add_listener(my_listener)
     
    pubnub.subscribe().channels(['lightning_ticker_BTC_JPY', 'lightning_ticker_FX_BTC_JPY']).execute()
    my_listener.wait_for_connect()

    bf_result = my_listener.wait_for_message_on('lightning_ticker_BTC_JPY')
    bf_data = bf_result.message
    bf_timestamp = bf_data['timestamp'][:26].replace('T',' ')

    fx_result = my_listener.wait_for_message_on('lightning_ticker_FX_BTC_JPY')
    fx_data = fx_result.message
    fx_timestamp = fx_data['timestamp'][:26].replace('T',' ')

    pubnub.unsubscribe().channels(['lightning_ticker_BTC_JPY', 'lightning_ticker_FX_BTC_JPY']).execute()
    my_listener.wait_for_disconnect()

    cc_req = requests.get(COINCHECK)
    cc_data = cc_req.json()

    qo_req = requests.get(QUOINE)
    qo_data = qo_req.json()

    zf_req = requests.get(ZAIF)
    zf_data = zf_req.json()

    bb_req = requests.get(BTCBOX)
    bb_data = bb_req.json()
    
    """ bidを集計（FX,krは除外） """
    bf_bid = bf_data['best_bid']
    cc_bid = cc_data['bid']
    qo_bid = qo_data['market_bid']
    zf_bid = zf_data['bid']
    bb_bid = bb_data['buy']

    bid_max = bf_bid
    bid_max_code = 'BF'
    if (bid_max < cc_bid):
        bid_max = cc_bid
        bid_max_code = 'CC'
    if (bid_max < qo_bid):
        bid_max = qo_bid
        bid_max_code = 'QO'
    if (bid_max < zf_bid):
        bid_max = zf_bid
        bid_max_code = 'ZF'
    if (bid_max < bb_bid):
        bid_max = bb_bid
        bid_max_code = 'BB'

    bid_min = bf_bid
    bid_min_code = 'BF'
    if (bid_min > cc_bid and cc_bid > 0):
        bid_min = cc_bid
        bid_min_code = 'CC'
    if (bid_min > qo_bid and qo_bid > 0):
        bid_min = qo_bid
        bid_min_code = 'QO'
    if (bid_min > zf_bid and zf_bid > 0):
        bid_min = zf_bid
        bid_min_code = 'ZF'
    if (bid_min > bb_bid and bb_bid > 0):
        bid_min = bb_bid
        bid_min_code = 'BB'

    bid_diff = bid_max - bid_min
    
    """ askを集計（FX,krは除外） """
    bf_ask = bf_data['best_ask']
    cc_ask = cc_data['ask']
    qo_ask = qo_data['market_ask']
    zf_ask = zf_data['ask']
    bb_ask = bb_data['sell']

    ask_max = bf_ask
    ask_max_code = 'BF'
    if (ask_max < cc_ask):
        ask_max = cc_ask
        ask_max_code = 'CC'
    if (ask_max < qo_ask):
        ask_max = qo_ask
        ask_max_code = 'QO'
    if (ask_max < zf_ask):
        ask_max = zf_ask
        ask_max_code = 'ZF'
    if (ask_max < bb_ask):
        ask_max = bb_ask
        ask_max_code = 'BB'

    ask_min = bf_ask
    ask_min_code = 'BF'
    if (ask_min > cc_ask and cc_ask > 0):
        ask_min = cc_ask
        ask_min_code = 'CC'
    if (ask_min > qo_ask and qo_ask > 0):
        ask_min = qo_ask
        ask_min_code = 'QO'
    if (ask_min > zf_ask and zf_ask > 0):
        ask_min = zf_ask
        ask_min_code = 'ZF'
    if (ask_min > bb_ask and bb_ask > 0):
        ask_min = bb_ask
        ask_min_code = 'BB'

    ask_diff = ask_max - ask_min

    sql = "INSERT INTO btc (bf_total_bid_depth, bf_total_ask_depth, bf_ltp, \
            bf_tick_id, bf_volume, bf_best_bid, bf_best_ask_size, \
            bf_volume_by_product, bf_product_code, bf_timestamp, \
            bf_best_bid_size, bf_best_ask, \
            fx_total_bid_depth, fx_total_ask_depth, fx_ltp, \
            fx_tick_id, fx_volume, fx_best_bid, fx_best_ask_size, \
            fx_volume_by_product, fx_product_code, fx_timestamp, \
            fx_best_bid_size, fx_best_ask, \
            cc_last,cc_bid,cc_ask,cc_high,cc_low,cc_volume,cc_timestamp, \
            qo_id,qo_product_type,qo_code,qo_name,qo_market_ask,qo_market_bid, \
            qo_indicator,qo_currency,qo_currency_pair_code,qo_symbol,qo_fiat_minimum_withdraw, \
            qo_pusher_channel,qo_taker_fee,qo_maker_fee,qo_low_market_bid,qo_high_market_ask, \
            qo_volume_24h,qo_last_price_24h,qo_last_traded_price,qo_last_traded_quantity, \
            qo_quoted_currency,qo_base_currency,qo_exchange_rate, \
            zf_last,zf_high,zf_low,zf_vwap,zf_volume,zf_bid,zf_ask, \
            bb_high,bb_low,bb_buy,bb_sell,bb_last,bb_vol, \
            bid_max, bid_max_code, bid_min, bid_min_code, bid_diff, \
            ask_max, ask_max_code, ask_min, ask_min_code, ask_diff, created) \
            VALUES ( \
            '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',\
            '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',\
            '%s','%s','%s','%s','%s','%s','%s', \
            '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s', \
            '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s', \
            '%s','%s','%s', \
            '%s','%s','%s','%s','%s','%s','%s', \
            '%s','%s','%s','%s','%s','%s', \
            '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',CURRENT_TIMESTAMP \
            )" \
            % (bf_data['total_bid_depth'], bf_data['total_ask_depth'], bf_data['ltp'], \
            bf_data['tick_id'], bf_data['volume'], bf_data['best_bid'], bf_data['best_ask_size'], \
            bf_data['volume_by_product'], bf_data['product_code'], bf_timestamp, \
            bf_data['best_bid_size'], bf_data['best_ask'], \
            fx_data['total_bid_depth'], fx_data['total_ask_depth'], fx_data['ltp'], \
            fx_data['tick_id'], fx_data['volume'], fx_data['best_bid'], fx_data['best_ask_size'], \
            fx_data['volume_by_product'], fx_data['product_code'], fx_timestamp, \
            fx_data['best_bid_size'], fx_data['best_ask'], \
            cc_data['last'],cc_data['bid'],cc_data['ask'],cc_data['high'],cc_data['low'],cc_data['volume'],datetime.datetime.fromtimestamp(cc_data['timestamp']), \
            qo_data['id'],qo_data['product_type'],qo_data['code'],qo_data['name'],qo_data['market_ask'],qo_data['market_bid'], \
            qo_data['indicator'],qo_data['currency'],qo_data['currency_pair_code'],qo_data['symbol'],qo_data['fiat_minimum_withdraw'], \
            qo_data['pusher_channel'],qo_data['taker_fee'],qo_data['maker_fee'],qo_data['low_market_bid'],qo_data['high_market_ask'], \
            qo_data['volume_24h'],qo_data['last_price_24h'],qo_data['last_traded_price'],qo_data['last_traded_quantity'], \
            qo_data['quoted_currency'],qo_data['base_currency'],qo_data['exchange_rate'], \
            zf_data['last'],zf_data['high'],zf_data['low'],zf_data['vwap'],zf_data['volume'],zf_data['bid'],zf_data['ask'], \
            bb_data['high'],bb_data['low'],bb_data['buy'],bb_data['sell'],bb_data['last'],bb_data['vol'], \
            bid_max, bid_max_code, bid_min, bid_min_code, bid_diff, ask_max, ask_max_code, ask_min, ask_min_code, ask_diff)

    stmt = dbh.cursor()

    stmt.execute(sql)
    dbh.commit()
    
    stmt.close()
    dbh.close()

    


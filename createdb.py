# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

import sqlite3

DB = 'bitflyer.db'

if __name__ == '__main__':
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    sql = "create table btcfx (bc_total_bid_depth, bc_total_ask_depth, bc_ltp, \
            bc_tick_id, bc_volume, bc_best_bid, bc_best_ask_size, \
            bc_volume_by_product, bc_product_code, bc_timestamp, \
            bc_best_bid_size, bc_best_ask, \
            fx_total_bid_depth, fx_total_ask_depth, fx_ltp, \
            fx_tick_id, fx_volume, fx_best_bid, fx_best_ask_size, \
            fx_volume_by_product, fx_product_code, fx_timestamp, \
            fx_best_bid_size, fx_best_ask, \
            diff_bid, diff_ask, created);"
    cur.execute(sql)

    conn.commit()
    conn.close()

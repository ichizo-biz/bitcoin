create table btc (
id BIGINT NOT NULL AUTO_INCREMENT,

bf_total_bid_depth DECIMAL(15,8),
bf_total_ask_depth DECIMAL(15,8),
bf_ltp DECIMAL(10,1),
bf_tick_id BIGINT,
bf_volume DECIMAL(15,8),
bf_best_bid DECIMAL(10,3),
bf_best_ask_size DECIMAL(12,8),
bf_volume_by_product DECIMAL(15,8),
bf_product_code VARCHAR(12),
bf_timestamp datetime,
bf_best_bid_size DECIMAL(12,8),
bf_best_ask DECIMAL(10,3),

fx_total_bid_depth DECIMAL(15,8),
fx_total_ask_depth DECIMAL(15,8),
fx_ltp DECIMAL(10,1),
fx_tick_id BIGINT,
fx_volume DECIMAL(15,8),
fx_best_bid DECIMAL(10,3),
fx_best_ask_size DECIMAL(12,8),
fx_volume_by_product DECIMAL(15,8),
fx_product_code VARCHAR(12),
fx_timestamp datetime,
fx_best_bid_size DECIMAL(12,8),
fx_best_ask DECIMAL(10,3),

cc_last DECIMAL(10,3),
cc_bid DECIMAL(10,3),
cc_ask DECIMAL(10,3),
cc_high DECIMAL(10,3),
cc_low DECIMAL(10,3),
cc_volume DECIMAL(13,8),
cc_timestamp datetime,

qo_id int,
qo_product_type VARCHAR(20),
qo_code VARCHAR(8),
qo_name VARCHAR(20),
qo_market_ask DECIMAL(10,3),
qo_market_bid DECIMAL(10,3),
qo_indicator smallint,
qo_currency VARCHAR(4),
qo_currency_pair_code VARCHAR(8),
qo_symbol VARCHAR(2),
qo_fiat_minimum_withdraw DECIMAL(10,3),
qo_pusher_channel VARCHAR(32),
qo_taker_fee DECIMAL(5,2),
qo_maker_fee DECIMAL(5,2),
qo_low_market_bid DECIMAL(10,3),
qo_high_market_ask DECIMAL(10,3),
qo_volume_24h DECIMAL(15,8),
qo_last_price_24h DECIMAL(10,3),
qo_last_traded_price DECIMAL(10,3),
qo_last_traded_quantity DECIMAL(12,8),
qo_quoted_currency VARCHAR(4),
qo_base_currency VARCHAR(4),
qo_exchange_rate DECIMAL(22,20),

zf_last DECIMAL(10,3),
zf_high DECIMAL(10,3),
zf_low DECIMAL(10,3),
zf_vwap DECIMAL(11,4),
zf_volume DECIMAL(15,8),
zf_bid DECIMAL(10,3),
zf_ask DECIMAL(10,3),

bb_high DECIMAL(10,3),
bb_low DECIMAL(10,3),
bb_buy DECIMAL(10,3),
bb_sell DECIMAL(10,3),
bb_last DECIMAL(10,3),
bb_vol DECIMAL(15,8),

kr_a_price DECIMAL(10,3),
kr_a_volume DECIMAL(13,8),
kr_b_price DECIMAL(10,3),
kr_b_volume DECIMAL(13,8),
kr_c_price DECIMAL(10,3),
kr_c_volume DECIMAL(13,8),
kr_v_today DECIMAL(13,8),
kr_v_24 DECIMAL(13,8),
kr_p_today DECIMAL(10,3),
kr_p_24 DECIMAL(10,3),
kr_t_today int,
kr_t_24 int,
kr_l_today DECIMAL(10,3),
kr_l_24 DECIMAL(10,3),
kr_h_today DECIMAL(10,3),
kr_h_24 DECIMAL(10,3),
kr_o DECIMAL(10,3),

bid_max DECIMAL(10,3),
bid_max_code VARCHAR(2),
bid_min DECIMAL(10,3),
bid_min_code VARCHAR(2),
bid_diff DECIMAL(11,4),
ask_max DECIMAL(10,3),
ask_max_code VARCHAR(2),
ask_min DECIMAL(10,3),
ask_min_code VARCHAR(2),
ask_diff DECIMAL(11,4),
created datetime,
primary key(id)
);

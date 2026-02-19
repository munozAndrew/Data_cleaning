Kalshi:
The dataset had 2 main tables (the ones i would be focusing on)
Important columns are ticker, event_ticker, title, result, volume, last_price, and close_time.
Trades has one row per transaction inside a market. Important columns are trade_id, ticker, count, yes_price, taker_side, and created_time. 
The tables join on ticker.
A very small subset of markets don't have a result (marked empty, 16 out of 10k entries). If there is no result, the market either never resolves or is still active at the time the data was scraped. These cant be used for my use case because I need the outcome as well. I must filter to only markets where result is yes or no.

Most of the dataset is sports markets like NFL, NBA, and parlays. My hypothesis is about question complexity affecting accuracy. That is more interesting in markets where the wording and structure actually vary, like economics, weather, politics, misc.. I need to filter out sports heavy event tickers and focus on categories like FED, INFL, EURUSD, HURCAT, PAYROLLS, and APRPOTUS.

There are a lot columns that are not needed for testing. This includse order book fields like yes_bid, yes_ask, no_bid, no_ask, short term metrics like volume_24h, and timestamps like open_time, created_time, and _fetched_at. open_interest is also not needed. I really only need the columns: ticker, event_ticker, title, result, volume, last_price, and close_time.

After looking through, the dataset should support the hypothesis. The title column gives question text, which I can use to measure complexity. The result and last_price let me measure accuracy by comparing the final traded price to the true outcome. The main limit is that I can only measure accuracy on markets that both resolved and had real trading activity, but whats cool with this dataset is I can download more, so even if its a smaller subset of the actual 36GB I am still able to get a more accurate conclusion. 

Polymarket:

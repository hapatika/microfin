import yfinance as yf 
import numpy as np 
import pandas as pd
import datetime as dt 

def get_data(assets: list, startdate = (dt.datetime.today - dt.timedelta(days=504)), enddate=dt.datetime.today):
  # Returns: dates, adj_close, returns, log_returns, raw_data
  data = yf.download(assets, start = startdate, end=enddate)
  dates = data.index.to_numpy()
  adj_close = data['Close'].to_numpy()
  cov = data['Close'].corr()
  returns = data['Close'].pct_change()
  log_returns = np.log(1 + returns)
  return dates, adj_close, returns.to_numpy(), log_returns.to_numpy(), cov.to_numpy(), data.to_numpy()


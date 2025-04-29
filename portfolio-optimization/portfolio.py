# Imports
import numpy as np
import numpy.typing as npt
import numba as nb 
import pandas as pd 
import abc
import matplotlib.pyplot as plt
import datafetch 
import pmdarima
import arch

class TimeSeries:
  # n_obs is number of observations in the time series.
  # X is time series data, shape [n_obs, 2], column 1 is the date and collumn 2 is the data

  def __init__(self):
    self.n_obs: int
    self.X: npt.ArrayLike
    self.index: npt.ArrayLike
    self.data: npt.ArrayLike
    self.returns: npt.ArrayLike 
    self.log_returns: npt.ArrayLike
    self.adj_close: npt.ArrayLike
    self.correlation = 0

  def set_series_data(self, index, adj_close, returns, log_returns, correlation, data):
    self.index = index
    self.adj_close = adj_close
    self.returns = returns
    self.log_returns = log_returns
    self.correlation = correlation
    self.data = data

  def unconditional_mean(self):
    return np.mean(self.data)
  
  def unconditional_variance(self):
    return np.std(self.data)*np.std(self.data)

  def conditional_mean(self):
    pass

  def conditional_variance(self):
    pass

  def get_returns(self):
    return self.returns
  
  
  def separate_X(self): 
    self.data = self.X[:, 1]
    self.index =  self.X[:, 0]
    return 

  def calculate_returns(self):
    ret_data = np.diff(self.data)
    ret_index = self.index[1:]
    self.returns = np.concatenate((ret_index, ret_data), axis=1)
    print("Returns in time series.", self.returns)
    return 
  
  def ARMA(self):
    pmdarima.auto_arima()

  def GARCH(self):
    pass


# Portfolio Class 

class Portfolio:
  def __init__(self, initial_capital, n_assets, assets: list, weights: npt.ArrayLike):
    self.initial_capital: float = initial_capital
    self.n_assets: int = n_assets
    self.n_obs: int
    self.weights: npt.ArrayLike = weights 
    self.assets: list = assets
    self.returns: npt.ArrayLike 
    self.log_returns: npt.ArrayLike
    self.means: npt.ArrayLike
    self.assets_time_series = TimeSeries()
    self.portfolio_time_series = TimeSeries()
    self.initial_allocation: list 

  def get_data(self, startdate, enddate):
    dates, close, returns, log_returns, covariance, raw_data = datafetch.get_data(self.assets, startdate, enddate)
    self.assets_time_series.set_series_data(dates, close, returns, log_returns, covariance, raw_data)
    return 
  
  def construct_portfolio(self):
    self.initial_allocation = self.weights*self.initial_capital
    return

  def standardise_data(self):
    # Currency conversions
    pass 

  def historic_mean_returns(self) -> npt.ArrayLike:
    self.means = np.mean(self.returns)
    return 

  def variance(self):
    pass 

  def mc_simulations(self, n_sims = 1000, n_days = 252, method = "return", mean="unconditional"):
    # mean: "unconditional", models returns with historic unconditional mean data
    #         "ARMA" for conditional expectation modelling, then MC simulation for:
    # method: "log": log-normal returns, "return"
    if mean == "unconditional":
      if method == "return":
        ret = self.assets_time_series.get_returns()
        meanRet = np.mean(ret, axis = 1)
        meanMatrix = np.full(shape = (n_days, len(self.weights)), fill_value = meanRet).T
        portfolio_sim = np.full(shape=(n_days, self.n_sims), fill_value=0.0)
        for i in range(0, mc_sims):
          Z = np.random.normal(size=(T, len(weights)))
          L = np.linalg.cholesky(covMat)
          dailyReturns = meanMatrix + np.inner(L, Z)
          portfolio_sim[:, i] = np.cumprod(np.inner(self.weights, dailyReturns.T) + 1)*self.initial_capital
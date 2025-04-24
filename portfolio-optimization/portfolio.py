# Imports
import numpy as np
import numpy.typing as npt
import numba as nb 
import pandas as pd 
import abc
import matplotlib.pyplot as plt
import datafetch 

class TimeSeries:
  # n_obs is number of observations in the time series.
  # X is time series data, shape [n_obs, 2], column 1 is the date and collumn 2 is the data

  def __init__(self):
    self.n_obs: int
    self.X: npt.ArrayLike
    self.index: npt.ArrayLike
    self.data: npt.ArrayLike
    self.returns: npt.ArrayLike
  
  def unconditional_mean(self):
    pass
  
  def unconditional_variance(self):
    pass

  def conditional_mean(self):
    pass

  def conditional_variance(self):
    pass
  
  def separate_X(self): 
    self.data = self.X[:, 1]
    self.index =  self.X[:, 0]
    return 

  def calculate_returns(self):
    ret_data = np.diff(self.data)
    ret_index = self.index[1:]
    self.returns = np.concatenate((ret_index, ret_data), axis=1)
    print("Returns", self.returns)
    return 


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

  def get_data(self, startdate, enddate):
    

  def standardise_data(self):


  def historic_mean_returns(self) -> npt.ArrayLike:
    self.means = np.mean(self.returns)
    return 

  def variance(self):
    pass 

  def mc_simulations(self, n_sims = 1000, n_days = 252, method = "log"):
    
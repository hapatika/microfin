# Imports
import numpy as np
import numpy.typing as npt
import numba as nb 
import pandas as pd 
import abc
import matplotlib.pyplot as plt 

# Optimizer Class 

class Optimizer:
  def __init__(self):
    pass

class MeanVariance(Optimizer):
  # Objective is to maximise the first moment - the expectation of the portfolio returns and minimize the second momemnt - the variance. 
  # Computationally tractable when 
  def __init__(self):
    pass


class ADMM(Optimizer):
  pass

class CoordinateDescent(Optimizer):
  pass
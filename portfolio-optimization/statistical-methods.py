# Imports
import numpy as np
import numpy.typing as npt
import numba as nb 
import pandas as pd 
import matplotlib.pyplot as plt 

# Methods Class 

class StatisticalMethod:
  def __init__(self):
    self.data: npt.ArrayLike # can't generalise this between MC 
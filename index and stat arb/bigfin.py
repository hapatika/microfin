import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf
import csv
import matplotlib.dates as mdates 
import seaborn as sns
from scipy.stats import norm, gmean, cauchy
import sktime
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox
from sklearn.metrics import mean_absolute_error, mean_squared_error
from arch import arch_model
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import acf
from scipy.linalg import solve
from scipy import stats
from scipy.optimize import minimize, rosen, rosen_der
from scipy.stats import probplot
from statsmodels.stats.diagnostic import het_arch
from numba import jit

# Get data in relevant pd dataframes 
def PreProcessing(filename):
  principal_df = pd.read_csv("./SP Top 50.csv")
  principal_df.head()

if __name__ == '__main__':
  print("Imports complete!\n")

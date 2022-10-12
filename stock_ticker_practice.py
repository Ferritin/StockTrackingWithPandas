import numpy as np
import pandas as pd
import yfinance as yf

#This creates a Ticker object that does lots of thing
msft = yf.Ticker("MSFT")

#msft.history creates a pandas data frame that contains all the stock information in the requested range
FiveDayHistory = msft.history(period="5d")

#This only lists the prices at Open and stores that dataframe at a
FiveDayOpenHistory = FiveDayHistory["Open"]

#Prints a
print (FiveDayOpenHistory)

#Prints the average open price of a
print (FiveDayOpenHistory.mean())

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

# For reading stock data from yahoo
from pandas_datareader.data import DataReader

# For time stamps
from datetime import datetime

#Dow Jones 30 stocks
stock_data = {}
dow_30 = ['AAPL', 'AMGN', 'AXP', 'BA', 'CAT', 'CRM', 'CSCO', 'CVX', 'DIS',  'DOW', 
          'GS', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'JPM', 'KO', 'MCD', 'MMM', 
          'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH', 'V', 'VZ', 'WBA', 'WMT']

# Set up End and Start times for data grab
end = datetime.now()
start = datetime(end.year - 30, end.month, end.day)

#For loop for grabing yahoo finance data and setting it as a dataframe. 
#If Yahoo data is unavailble it attempts to check Investors Exchange (IEX).
for stock in dow_30:   
    # Set DataFrame as the Stock Ticker
    try:
        stock_data[stock] = DataReader(stock, 'yahoo', start, end)
    except:
        stock_data[stock] = DataReader(stock, 'iex', start, end)
    
company_list = [AAPL, AMGN, AXP, BA, CAT, CRM, CSCO, CVX, DIS,  DOW, 
          GS, HD, HON, IBM, INTC, JNJ, JPM, KO, MCD, MMM, 
          MRK, MSFT, NKE, PG, TRV, UNH, V, VZ, WBA, WMT]

company_name = ["APPLE", "AMGEN", "AMERICAN EXPRESS", "BOEING", "CATERPILLAR", 
                "SALESFORCE", "CISCO", "CHEVRON", "DISNEY", "DOW",
               "GOLDMAN SACHS", "HOME DEPOT", "HONEYWELL", "IBM", "INTEL",
                "JOHNSON & JOHNSON", "CHASE", "COKE", "MCDONALDS", "3M",
               "MERCK", "MICROSOFT", "NIKE", "PROCTER & GAMBLE", "THE TRAVELERS COMPANY",
                "UNITEDHEALTH", "VISA", "VERIZON", "WALGREENS", "WALMART"]

for company, name in zip(company_list, company_name):
    company["company_name"] = name
    
df = pd.concat(company_list, axis=0)

df.to_csv('stock_data.csv')
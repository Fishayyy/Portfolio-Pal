# For reading stock data from yahoo
import pandas as pd
from pandas_datareader.data import DataReader

# For time stamps
from datetime import datetime, timedelta

#Dow Jones 30 stocks
stock_data = {}
YEARS_FROM_PRESENT = 15
dow_30 = ['AAPL', 'AMGN', 'AXP', 'BA', 'CAT', 'CRM', 'CSCO', 'CVX', 'DIS',  'DOW', 
          'GS', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'JPM', 'KO', 'MCD', 'MMM', 
          'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH', 'V', 'VZ', 'WBA', 'WMT']

# Set up End and Start times for data grab
# We don't want today, because the closing price isn't final yet
end = datetime.now() - timedelta(days=1)
start = datetime(end.year - YEARS_FROM_PRESENT, end.month, end.day)

#For loop for grabing yahoo finance data and setting it as a dataframe. 
for stock in dow_30:   
    try:
        stock_data[stock] = DataReader(stock, 'yahoo', start, end)
    except:
        print(f"Unable to get data for {stock} ticker.")

company_name = ["APPLE", "AMGEN", "AMERICAN EXPRESS", "BOEING", "CATERPILLAR", 
                "SALESFORCE", "CISCO", "CHEVRON", "DISNEY", "DOW",
               "GOLDMAN SACHS", "HOME DEPOT", "HONEYWELL", "IBM", "INTEL",
                "JOHNSON & JOHNSON", "CHASE", "COKE", "MCDONALDS", "3M",
               "MERCK", "MICROSOFT", "NIKE", "PROCTER & GAMBLE", "THE TRAVELERS COMPANY",
                "UNITEDHEALTH", "VISA", "VERIZON", "WALGREENS", "WALMART"]

for ticker, com_name in zip(stock_data, company_name):
    stock_data[ticker]['company_name'] = com_name
    stock_data[ticker].to_csv(f'./stock data/{ticker}.csv')
    

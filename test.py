import os
import pandas as pd

# For reading stock data from yahoo
from pandas_datareader.data import DataReader

# For time stamps
from datetime import datetime, timedelta


# The DowJones 30 index we'll use for this analysis
dow_30 = ['AAPL', 'AMGN', 'AXP', 'BA', 'CAT', 'CRM', 'CSCO', 'CVX', 'DIS',  'DOW', 
          'GS', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'JPM', 'KO', 'MCD', 'MMM', 
          'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH', 'V', 'VZ', 'WBA', 'WMT']

company_name = ["APPLE", "AMGEN", "AMERICAN EXPRESS", "BOEING", "CATERPILLAR", 
                "SALESFORCE", "CISCO", "CHEVRON", "DISNEY", "DOW",
               "GOLDMAN SACHS", "HOME DEPOT", "HONEYWELL", "IBM", "INTEL",
                "JOHNSON & JOHNSON", "CHASE", "COKE", "MCDONALDS", "3M",
               "MERCK", "MICROSOFT", "NIKE", "PROCTER & GAMBLE", "THE TRAVELERS COMPANY",
                "UNITEDHEALTH", "VISA", "VERIZON", "WALGREENS", "WALMART"]

stock_data = {}

# Get last week of data
end = datetime.now() - timedelta(days=1)

for i in range(len(dow_30)):
    dataframe = pd.read_csv(f'./stock data/{dow_30[i]}.csv')
    date = end.strftime('%Y-%m-%d')
    if date not in dataframe['Date'].values:
        print(f"Updating {dow_30[i]}...")
        last_date = dataframe['Date'].iloc[-1]
        start = datetime.strptime(last_date, '%Y-%m-%d') + timedelta(days=1)
        try:
            new_data = DataReader(dow_30[i], 'yahoo', start, end)
        except:
            print(f"Unable to update {dow_30[i]} dataframe for date range {start} to {end}.")
        new_data['company_name'] = company_name[i]
        new_data['Date'] = ''
        for index in new_data.index:
            new_data.loc[index, 'Date'] = index.strftime('%Y-%m-%d')
        dataframe = dataframe.append(new_data, ignore_index=True)
        dataframe.to_csv(f'./stock data/{dow_30[i]}.csv', index=False)
    stock_data[dow_30[i]] = dataframe


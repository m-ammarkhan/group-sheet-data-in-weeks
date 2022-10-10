# Export your sheet as .csv or .xlxs

import pandas as pd
from datetime import datetime

# Relace '%Y-%m-%d' with '%Y-%m-%d %H:%M:%S'; If date contains time
dateparse = lambda x: datetime.strptime(x, '%Y-%m-%d')

# Replace 'try.csv' with your file path.
# Replace 'read_csv' with 'read_xlxs'; If google sheet is exported as .xlxs
df = pd.read_csv('try.csv', parse_dates=['Timestamp'], date_parser=dateparse)
df.set_index('Timestamp', inplace=True)
print('\nDataframe without grouping\n------------------------------')
print(df)

# 'W-MON'; weekly frequency (Mondays)
# Replace 'Question1' with column containing textual data
# Replace 'Question2' with column containing numeric data
dfTemp = df.groupby(pd.Grouper(freq='W-MON'), as_index=False).agg({'Question1': ', '.join, 'Question2': 'sum'})
print('\nGroup by Week\n------------------------------------------------------------')
print(dfTemp)

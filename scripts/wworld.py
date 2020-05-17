import pandas as pd                                         #needed for dataframe

wview_df = pd.read_csv('../data/worldwide-aggregated.csv',parse_dates=['Date'])
print('+-' * 30)
print(wview_df)

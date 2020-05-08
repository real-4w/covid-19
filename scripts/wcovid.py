import pandas as pd                                         #needed for dataframe
import matplotlib.pyplot as plt                             #needed for plot

covid_df = pd.read_csv('../data/countries-aggregated.csv',parse_dates=['Date'])              #read csv
nz_df = (covid_df.loc[covid_df['Country'] == "New Zealand"])
nz_df = (nz_df.loc[covid_df['Confirmed'] > 0 ])

us_df = (covid_df.loc[covid_df['Country'] == "US"])
us_df = (us_df.loc[covid_df['Confirmed'] > 0 ])

print('+-' * 30)
print("Earliest infection NZ : ", nz_df['Date'].min())
print("Latest data: ", nz_df['Date'].max())
print(nz_df)
print('+-' * 30)
print("Earliest infection US : ", us_df['Date'].min())
print("Latest data: ", us_df['Date'].max())
print(us_df)
print('+-' * 30)

nz_df.plot(x='Date', y=['Confirmed', 'Recovered', 'Deaths'])
us_df.plot(x='Date', y=['Confirmed', 'Recovered', 'Deaths'])

plt.show()

import pandas as pd                                         #needed for dataframe
import matplotlib.pyplot as plt                             #needed for plot

covid_df = pd.read_csv('../data/countries-aggregated.csv',parse_dates=['Date'])              #read csv
nz_df = (covid_df.loc[covid_df['Country'] == "New Zealand"])
nz_df = (nz_df.loc[covid_df['Confirmed'] > 0 ])

print('+-' * 30)
print("Earliest infection NZ : ", nz_df['Date'].min())
print("Latest data: ", nz_df['Date'].max())
print(nz_df)
country = input("Compare with what country: ")
#Needs a check to see if country exits
other_df = (covid_df.loc[covid_df['Country'] == country])
other_df = (other_df.loc[covid_df['Confirmed'] > 0 ])


print('+-' * 30)
print(f"Earliest infection {country}", other_df['Date'].min())
print("Latest data: ", other_df['Date'].max())
print(other_df)
print('+-' * 30)

nz_df.plot(x='Date', y=['Confirmed', 'Recovered', 'Deaths'])
other_df.plot(x='Date', y=['Confirmed', 'Recovered', 'Deaths'])

plt.show()

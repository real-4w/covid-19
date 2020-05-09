import pandas as pd                                         #needed for dataframe
import matplotlib.pyplot as plt                             #needed for plot
import numpy

covid_df = pd.read_csv('../data/countries-aggregated.csv',parse_dates=['Date'])              #read country aggregated csv
nz_df = (covid_df.loc[covid_df['Country'] == "New Zealand"])
nz_df = (nz_df.loc[covid_df['Confirmed'] > 0 ])             #filter dates with no COVID

reference_df = pd.read_csv('../data/reference.csv')
#print(reference_df)
nz_ref_df = (reference_df.loc[reference_df['Country_Region'] == "Netherlands"])
#print(nz_ref_df['Population'].values)
nz_df['Peeps'] = 4000000 #  (nz_ref_df['Population'].values)

print(nz_ref_df)
#print(nz_df)
print(nz_ref_df['Population'].values[0])

print('+-' * 30)
print("Earliest infection NZ : ", nz_df['Date'].min())
print("Latest data: ", nz_df['Date'].max())
print(nz_ref_df['Population'].values)

country = input("Compare with what country: ")
while not (covid_df['Country']==country).any():
    country = input("Compare with what country: ")

other_df = (covid_df.loc[covid_df['Country'] == country])
other_df = (other_df.loc[covid_df['Confirmed'] > 0 ])

print('+-' * 30)
print(f"Earliest infection {country}", other_df['Date'].min())
print("Latest data: ", other_df['Date'].max())
print(other_df)
print('+-' * 30)

#other_df = other_df.groupby('Date')

fig, axes = plt.subplots(nrows=2, ncols=2)
nz_df.plot(ax=axes[0,0], x='Date', y=['Confirmed', 'Recovered', 'Deaths'])
nz_df.plot(ax=axes[0,1], x='Date', y=['Deaths'])

other_df.plot(ax=axes[1,0],x='Date', y=['Confirmed', 'Recovered', 'Deaths'])
other_df.plot(ax=axes[1,1],x='Date', y=['Deaths'])

#nz_df.plot(x='Date', y=['Confirmed', 'Recovered', 'Deaths'])
#other_df.plot(x='Date', y=['Confirmed', 'Recovered', 'Deaths'])

plt.show()

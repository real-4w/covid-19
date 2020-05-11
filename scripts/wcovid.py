import pandas as pd                                         #needed for dataframe
import matplotlib.pyplot as plt                             #needed for plot

def print_data(country, country_df, country_ref_df):
    print('+-' * 30)
    print(f"Earliest infection in {country}: ", country_df['Date'].min())
    print(f"Latest data for {country}: ", country_df['Date'].max())
    print(f"Total population for {country}", country_ref_df['Population'].sum())
    print(f"Detailed reference data for {country}:")
    print(country_ref_df)
    print(country_df)

def calc_data (country_df, country_ref_df):
    print('+-' * 30)
    print('Calculating more data')
    country_df['Per 1'] = round(country_df['Deaths'] / country_df['Confirmed'] * 100, 4)
    print (country_df)


def print_death(country_df):
    d_name = country_df['Country'].values[0]
    d_max = country_df['Deaths'].max()
    d_patients = country_df['Confirmed'].max()            #should really be last value
    d_per1 = round(d_max / d_patients * 100, 4)
    d_pop = int(country_df['Population'].max())
    d_per2 = round(d_max / d_pop * 100, 4)
    d_per3 = round(d_patients / d_pop * 100, 4)
    print('+-' * 30)
    print(f"Total death {d_name} {d_max} out of {d_patients} COVID-19 patients ({d_per1}%).")
    print(f"Percentage of the of the polulation of {d_pop} with COVID {d_per3}%.")
    print(f"Percentage of the entire population that died because of COVID {d_per2}%.")


reference_df = pd.read_csv('../data/reference.csv')         #load reference data
covid_df = pd.read_csv('../data/countries-aggregated.csv',parse_dates=['Date'])    #read country aggregated csv

country1 = input("What country are we looking for: ")
while not (covid_df['Country']==country1).any():
    country1 = input("Try again: what country are we looking for: ")

c1_df = (covid_df.loc[covid_df['Country'] == country1])     #pick data for country1
c1_df = (c1_df.loc[covid_df['Confirmed'] > 0 ])             #filter dates with no COVID
c1_ref_df = (reference_df.loc[reference_df['Country_Region'] == country1])
c1_df['Population'] = (c1_ref_df['Population'].values[0])   #first line in file has total, no need for sum())
print_data(country1, c1_df, c1_ref_df)


country2 = input("Compare with what country: ")
while not (covid_df['Country']==country2).any():
    country2 = input("Try, again: compare with what country: ")

c2_df = (covid_df.loc[covid_df['Country'] == country2])     #pick data for country2
c2_df = (c2_df.loc[covid_df['Confirmed'] > 0 ])             #filter dates with no COVID
c2_ref_df = (reference_df.loc[reference_df['Country_Region'] == country2])
c2_df['Population'] = (c2_ref_df['Population'].values[0])

print_data(country2, c2_df, c2_ref_df)

calc_data(c1_df, c1_ref_df)
print ("post calc")
print (c1_df)

print_death(c1_df)
print_death(c2_df)

fig, axes = plt.subplots(nrows=2, ncols=2)
c1_df.plot(ax=axes[0,0], title=country1, x='Date', y=['Confirmed', 'Recovered', 'Deaths'])
c1_df.plot(ax=axes[0,1], title=country1, x='Date', y=['Deaths'])

c2_df.plot(ax=axes[1,0],title=country2, x='Date', y=['Confirmed', 'Recovered', 'Deaths'])
c2_df.plot(ax=axes[1,1],title=country2, x='Date', y=['Deaths'])

#elec_df.plot(y=['kWh', 'Export', 'Demand'])
#plt.scatter(d_per1, d_per2)

plt.show()

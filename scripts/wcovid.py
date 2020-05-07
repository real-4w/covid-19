import pandas as pd                                         #needed for dataframe
import matplotlib.pyplot as plt                             #needed for plot

fit_df = pd.read_csv('fitbit_202004.csv',parse_dates=['Date'], dayfirst=True, thousands=",")              #read csv
fit_df = fit_df.sort_values(['Date'])                       #sort by date & time
fit_df = fit_df.groupby('Date').sum()                       #group by date - 1 recods a day
fit_df['Distance'] = fit_df['Distance'] * 1000              #calculate distnace in meters

print('+-' * 30)
print(fit_df)
print('+-' * 30)
print("Number of rows loaded:", len(fit_df))
print("Number of steps for the month", fit_df['Steps'].sum())
print('+-' * 30)

fig, axes = plt.subplots(nrows=2, ncols=2)
fit_df.plot(ax=axes[0,0], y=['Calories Burned', 'Activity Calories'])
fit_df.plot(ax=axes[0,1], y=['Steps', 'Distance'])
fit_df.plot(ax=axes[1,0],y=['Minutes Lightly Active','Minutes Fairly Active','Minutes Very Active'])
fit_df.plot(ax=axes[1,1],y=['Minutes Sedentary'])

plt.show()
#end

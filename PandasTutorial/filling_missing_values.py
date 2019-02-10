import pandas as pd

#Reading the data from CSV with dates in a proper format


df = pd.read_csv("pandas/5_handling_missing_data_fillna_dropna_interpolate/weather_data.csv",
                 parse_dates = ["day"])
print(type(df.day[0]))

#Filling all the Missing Values with 0
new_df = df.fillna(0)
print(new_df)

#Filling the missing data particular the columns
new_df = df.fillna({
    'temperature' : 0,
    'windspeed' : 0,
    'event' : 'no event'
})

print(new_df)

#Filling the values by forward filling them
new_df = df.fillna(method = 'ffill')
print(new_df)

#Filling the values by forward filling them but forwarding values to some limit only
new_df = df.fillna(method = 'ffill',limit = 1)
print(new_df)

#Filling the values by forward filling them but horizontally
new_df = df.fillna(method = 'ffill',axis = 1)
print(new_df)

#Filling the values by backward filling them
new_df = df.fillna(method = 'bfill',limit=1,axis = 1)
print(new_df)

#Interpolating the value
new_df = df.interpolate()
print(new_df)

#Interpolating the value by better guess
df.set_index('day',inplace = True)
new_df = df.interpolate(method="time")
print(new_df)

#Dropping the rows with NaN value
new_df = df.dropna()
print(new_df)

#Dropping the rows will are all NaN
new_df = df.dropna(how="all")
print(new_df)

#Keeping only the rows which has atleast "n" non-NaN Values
new_df = df.dropna(thresh = 2)
print(new_df)

dt = pd.date_range("01-01-2017","31-01-2017")
idx = pd.DatetimeIndex(dt)
print(idx)
df = df.reindex(dt)
print(df)
import pandas as pd


#Reading CSV file for creating a dataframe
df = pd.read_csv("pandas/2_dataframe_basics/weather_data.csv")
# print(df[['temperature','windspeed']])


#Creating a dataFrame from Python Dictionary
data = {
    'student_id':[1,2,3,4,5],
    'name': ['Jitesh','Aman','Raghav','Harman','Madhav'],
    'branch': ['cse','ece','mech','cse','bio']
}

df_dict = pd.DataFrame(data)
# print(df_dict)
print(df_dict.shape)

#Printing rows from top
print(df.head())

#Printing from end
print(df.tail(3))

#Slicing on dataframe
print(df[1:4])

#Finding Max,Min Value
print("Max Temp:", df['temperature'].max())
print("Min Temp:", df['temperature'].min())
print("Mean of Temp:", df['temperature'].mean())
print("Standard Deviation of Temp:", df['temperature'].std())

#Print the statistics of data
print(df.describe())

#Conditionally Select Data
print(df[df['temperature'] >= 32])  #or     df[df.tempeature >= 32]

#Print the temperature and day where temp was max
print ( df[['day','temperature']][df.temperature == df.temperature.max()])

#Setting the index of the dataframe
print(df.set_index('event',inplace = True))

print(df.loc['Snow'])

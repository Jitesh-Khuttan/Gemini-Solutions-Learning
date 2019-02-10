import pandas as pd

df = pd.read_csv("pandas/7_group_by/weather_by_cities.csv")
# print(df)
#
grp = df.groupby('city')
#
# for city,city_df in grp:
#     grp.get_group(city)

print(grp.get_group('mumbai')['temperature'].max())
print(grp.get_group('new york')['temperature'].max())
print(grp.describe())


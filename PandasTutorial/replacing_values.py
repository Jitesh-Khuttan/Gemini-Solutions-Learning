import pandas as pd
import csv
import numpy as np

df = pd.read_csv("pandas/6_handling_missing_data_replace/weather_data.csv")
with open("pandas/6_handling_missing_data_replace/weather_data.csv",mode="r") as infile:
    reader = csv.reader(infile)
    header = next(reader,None)
    master_dict = { row[0] + "," + row[1] : row[2] for row in reader}

print("Header is: ", header)
print("Master_Dict is: ",master_dict)
#
# # print(df)
#
# #Replace all occurances of particular value
# new_df = df.replace([-99999,7],np.NaN)
# print(new_df)
#
# #Replacing values corresponding to particular columns
# new_df = df.replace({
#     'temperature' : -99999,
#     'event' : '0'
# },np.NaN)
# print(new_df)
#
# #Replacing particular values with some other particular values
# new_df = df.replace({
#     -99999 : np.NaN,
#     '0' : 'Sunny'
# })
# print(new_df)
#
# #Suppose our data is given something like : temp: 32 F, then we have to remove F using regex
# new_df = df.replace({
#     'temperature' : '[A-Za-z]'
# },'',regex = True)
#
#
# print(df.T.to_dict().values())
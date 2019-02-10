import pandas as pd

#Creating dataFrame from csv file
df_csv = pd.read_csv("pandas/3_different_ways_of_creating_dataframe/weather_data.csv")
print("Read from CSV")
print(df_csv)

#Creating dataframe from Excel File
df_xl = pd.read_excel("pandas/3_different_ways_of_creating_dataframe/weather_data.xlsx","Sheet1")
print("Read from Excel")
print(df_xl)

#Creating dataframe from Dictionaries
data_dict = {
'student_id':[1,2,3,4,5],
    'name': ['Jitesh','Aman','Raghav','Harman','Madhav'],
    'branch': ['cse','ece','mech','cse','bio']
}

df_dict = pd.DataFrame(data_dict)
print("Read from Dictionary")
print(df_dict)

#Creating a dataFrame from list of tuples (you need to provide column names too)
data_lst_tup = [
    (1,'Jitesh','cse'),
    (2,'Aman','ece'),
    (3,'Raghav','mech'),
    (4,'Harman','cse'),
]

df_lst_tup = pd.DataFrame(data_lst_tup,columns = ["Sid","Name","Branch"])
print("Created from list of tuples")
print(df_lst_tup)

#Creating from list of dictionaries
data_lst_dict = [
    {"Sid":1,"Name":"Jitesh","Branch":"CSE"},
    {"Sid":2,"Name":"Hitesh","Branch":"Mech"}
]

df_lst_dict = pd.DataFrame(data_lst_dict)
print("Created from list of dictionaries")
print(df_lst_dict)


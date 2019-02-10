import pandas as pd

df = pd.read_csv("pandas/4_read_write_to_excel/stock_data.csv")
# print(df)


#Suppose the header of your excel file starts from 2nd line.
df = pd.read_csv("pandas/4_read_write_to_excel/stock_data.csv",header=1)
# print(df)

#If you want to skip reading some rows from csv file
df = pd.read_csv("pandas/4_read_write_to_excel/stock_data.csv",skiprows=3)
# print(df)

#Suppose there is no header in your CSV file
df = pd.read_csv("pandas/4_read_write_to_excel/stock_data.csv",header=None)
# print(df)

#In the case where there is no header, you can manually provide a list of column name
df = pd.read_csv("pandas/4_read_write_to_excel/stock_data.csv",header=None,names = ["row1","row2","row3","row4","row5"])
# print(df)

#Supoose that you want to read only particular number of rows from the file (except header)
df = pd.read_csv("pandas/4_read_write_to_excel/stock_data.csv",nrows=3)
# print(df)

#Filling the particular values with NaN
df = pd.read_csv("pandas/4_read_write_to_excel/stock_data.csv",na_values = ["n.a.","not available"])
# print(df)

#Filling values with Nan Based on the particular column values
df = pd.read_csv("pandas/4_read_write_to_excel/stock_data.csv", na_values = {
    'eps' : ["not available","n.a."],
    'revenue' : [-1,"not available",'n.a.'],
    'people' : ["not available","n.a."],
    'price' : ["not available","n.a."]
})
print(df)


#Writing to a csv file
df.to_csv("new.csv")

#Write without index
df.to_csv("new.csv",index = False)

#Writing only particular columns in the file
df.to_csv("new.csv",columns = ["people","price"],index = False)

#Skipping the header while writing
df.to_csv("new.csv",header=False)

def convert_people(cell):
    if cell == "n.a.":
        return "Jitesh Khuttan"
    else:
        return cell

def convert_eps(cell):
    if cell == "not available":
        return "NO"
    else:
        return cell
#Converters during reading of the file
df = pd.read_csv("pandas/4_read_write_to_excel/stock_data.csv",converters = {
    'people' : convert_people,
    'eps' : convert_eps
})

print(df)
import pandas as pd
import matplotlib
import os
from datetime import datetime

#read in csv data for /Cleaned/DOGEUSDT-1m-2019-07.csv and save to dataframe
# data_path = os.getcwd() +  "/Cleaned/DOGEUSDT-1m-2019-07.csv"
# first_df = pd.read_csv(data_path)
#print(first_df.head())

end_year = 21
end_month = 5
data_path = os.getcwd() +  "/Cleaned/DOGEUSDT-1m-20"
current_year = 19
current_month = 7

if current_month < 10:
        full_path = data_path + str(current_year) +"-0"  + str(current_month) + ".csv"   
else:
        full_path = data_path + str(current_year) +"-"  + str(current_month) + ".csv"   
first_df = pd.read_csv(full_path)

current_month = current_month + 1


while (end_year != current_year or end_month != current_month):
    if current_month < 10:
        full_path = data_path + str(current_year) +"-0"  + str(current_month) + ".csv"   
    else:
        full_path = data_path + str(current_year) +"-"  + str(current_month) + ".csv"   
    temp_df = pd.read_csv(full_path)
    frames = [first_df, temp_df]
    first_df = pd.concat(frames)
    
    current_month = current_month + 1
    if current_month >= 13: 
        current_year = current_year + 1
        current_month = 1
    
    print(len(first_df.index))


print(first_df.head())

milli = 1562328240000
temp = pd.to_datetime(milli, unit='ms').to_pydatetime()
print(temp.strftime('%H:%M:%S'))


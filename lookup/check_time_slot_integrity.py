import pandas as pd
import datetime as dt
import numpy as np
from pandas._libs.hashtable import duplicated

def get_time_slots():
    t = dt.datetime(year=2023,month=1,day=1,hour=0,minute=0)
    time_slots = [t.strftime("%H%M%S")]
    while (t != dt.datetime(year=2023,month=1,day=1,hour=23,minute=45)):
        t= t + dt.timedelta(minutes=15)
        time_slots.append(t.strftime("%H%M%S"))
    return time_slots

df = pd.read_csv("./gkg_files.csv")

time_slots = get_time_slots()
year_month_date = "20150218"
cur_time_list = []

# count_stat = pd.DataFrame() 
count = 0
count1 = 0
for i in df.itertuples():
    if year_month_date != i[1][37:45]:
        year_month_date = i[1][37:45]
        print(cur_time_list)
        if cur_time_list != time_slots:
            print(False)
            count +=1
        else:
            print(True)
            count1 +=1
        cur_time_list.clear()
    k = i[1][45:51]
    cur_time_list.append(k)

print(count1)
print(count)

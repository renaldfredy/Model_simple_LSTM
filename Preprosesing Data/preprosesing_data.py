import pandas as pd 
import numpy as np

# Memberi nama kolom
# nama_kolom = "0"
# for i in range(1,409):
# 	nama_kolom += ","
# 	nama_kolom += str(i)
# 	nama_kolom += " "
# colnames=[nama_kolom]

# Membuka file "csv"
data = pd.read_csv("TEXT.csv", header=None)

# Menghapus baris yang ada NA
data = data.dropna()

# Menulis ke CSV
export_csv = data.to_csv('Text_No_NA.csv',header=True) 

# Menghitung jumlah baris
print(data[1].count()) 
print(data[1].sum()) 
print(data[1].mean())

# print(data.itertuples())

# row_list = []

# for rows in data.itertuples():
# 	my_list =


# Menghitung jumlah semua

# ========== Membuat indeks bulan ========================================
awal = "1982-12"
awal = pd.to_datetime(awal)
from pandas.tseries.offsets import DateOffset
add_dates = [awal + DateOffset(months=x) for x in range(1,409) ]
# future_dates = pd.DataFrame(index=add_dates[1:],columns=df.columns)
# =======================================================================
bulan = []
dt = []
rata2= []
for i in range(1,409):
	bulan.append("bulan_"+str(i))
	dt.append((data[i].sum()))
	rata2.append((data[i].mean()))

dict = {'bulan': add_dates, 'data':dt, 'rata2': rata2}
df = pd.DataFrame(dict)

df.to_csv('file1.csv', header=True)

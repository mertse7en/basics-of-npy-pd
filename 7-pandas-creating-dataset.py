# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:56:12 2019

@author: Merts
"""

city = ["Bursa","Ankara"]
population = ["111", "222"]
list_label = ["city","population"]
list_col = [city,population]

zipped = list(zip(list_label,list_col))
data_dict = dict(zipped)
df = pd.DataFrame(data_dict)
print(df)
print(type(df))
print("-----")

#add new columns
df["baskent"] = ["osmangazi","çankaya"]
print(df)
print("-----")

# Broadcasting
df["havaalanısayisi"] = 0 #Broadcasting = whole columns
print(df)
print("-----")



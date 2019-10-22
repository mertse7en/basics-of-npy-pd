# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 17:55:36 2019
 We will use df
df
treatment	gender	response	age
0	A	F	10	15
1	A	M	45	4
2	B	F	5	72
3	B	M	9	65
# according to treatment take means of other features
df.groupby("treatment").mean()   # mean is aggregation / reduction method
# there are other methods like sum, std,max or min
response	age
treatment		
A	27.5	9.5
B	7.0	68.5
# we can only choose one of the feature
df.groupby("treatment").age.max() 
treatment
A    15
B    72
Name: age, dtype: int64
# Or we can choose multiple features
df.groupby("treatment")[["age","response"]].min() 
@author: Merts
"""

from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd        #dataframe
#bunu calıstıramadım spyderden(platformdan) dolayıdır belki you can check later

data = pd.read_csv("veriler.csv")
#creating dictionary
dic = {"treatment":["A","A","B","B"],"gender":["F","M","F","M"],"response":[10,45,5,9],"age":[15,4,72,65]}

df = pd.DataFrame(dic)

df.pivot(index="treatment",columns="gender",values="response")

print(df)

print(df.groupby("treatment").mean())
print(df)

print(df.info())
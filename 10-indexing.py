# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 01:27:17 2019

@author: Merts
"""

from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd        #datafram
from sklearn.metrics import confusion_matrix


data = pd.read_csv("veriler.csv")

print(data)
#ı couldnt work it if you need check quickly
data["boy"].apply(lambda n : n+300)
data.boy.apply(lambda n : n+300)

print(data.index.name)
data.index.name = "#"


print(data)


data1 = data.set_index(["boy","kilo"])
data1.head(100) 

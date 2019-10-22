# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 01:03:48 2019

@author: Merts
"""


from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd        #datafram
from sklearn.metrics import confusion_matrix


data = pd.read_csv("eksikveriler.csv")

data1 = data.loc[: , ["boy" , "kilo"]]
data1.plot(subplots = True) #subplots true 2 ayrı diagramda gösterir

#scatter x ye kordinat düzleminde nokta olarak
data1.plot(kind = "scatter",x="boy",y = "kilo")
plt.show()


#histogram şeklinde 
data.plot(kind = "hist",y = "yas",bins = 50,range= (0,100),normed = True)
plt.show()

print(data.describe())

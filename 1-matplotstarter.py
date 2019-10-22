# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 00:04:36 2019

@author: Merts
"""

from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd        #datafram
from sklearn.metrics import confusion_matrix


data = pd.read_csv("veriler.csv")


# scatter şeklinde veriyi visualize
# x y visualize etcegimiz attrslar ,alpha opaclık veiryo 
data.plot(kind = "scatter" , x = "boy" , y = "kilo" , alpha = 1,color = 'red' ) 
plt.xlabel("boy")
plt.xlabel("kilo")
plt.show()


#historical şekilde 
data.boy.plot(kind = 'hist',bins = 50,figsize = (6,6))
plt.show()


#plt.clf --> bı oncekı diagramı temizlemek istersen plt.clf()
plt.clf()

a = data["kilo"] > 180






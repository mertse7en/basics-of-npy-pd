# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:18:18 2019

@author: Merts
"""

from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd        #datafram
from sklearn.metrics import confusion_matrix


data = pd.read_csv("veriler.csv")


#show it
print(data[np.logical_and(data["boy"] > 150 , data["kilo"] > 50)])


#tru false 
print((data["boy"] > 170) & (data["kilo"] >60 ))



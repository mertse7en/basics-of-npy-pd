# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:18:10 2019

@author: Merts
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:21:33 2019
Cok gü
@author: Merts
"""

from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd        #datafram
from sklearn.metrics import confusion_matrix


data = pd.read_csv("eksikveriler.csv")


print("data info : ",data.info()) #genel info
print("data head :",data.head())  ## show us first 5 sentence
print("data tail :",data.tail())   ## son 5 satırı gösterir


print("data shape :",data.shape) ## satır ve sütün sayısını verir


print(data.describe())


print(data['ulke'].value_counts(dropna =False))    ##freakans gibi bişey verir
print(data['yas'].value_counts(dropna =False))  
print("-----------------")  

##With normalize set to True, returns the relative frequency by dividing all values by the sum of values.
## if we set dropna "false" we can also see nan variables

print(data['yas'].value_counts(dropna =True))


# buna cok bakmadım you can check it if you need
data.boxplot(column='boy',by = 'kilo')



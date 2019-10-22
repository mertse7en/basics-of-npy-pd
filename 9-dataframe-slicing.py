# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 01:11:31 2019

@author: Merts
#####
data loc dataframe e ^very important
data iloc numpy.ndrayye #######################
"""

from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd        #datafram
from sklearn.metrics import confusion_matrix


data = pd.read_csv("veriler.csv")


# Difference between selecting columns: series and dataframes
#bu cok onemli bunu kafana yaz amua goıyim
print(type(data["boy"]))     # series
print(type(data[["boy"]]))   # data frames

#its imp
#difference between dataloc and datailoc
#locla "boy " diye ayrıdım
#ama ilocla "boy" diye ayrıamadım
#iloc adı ustunde integer location cannot do slice indexing on <class 'pandas.core.indexes.base.Index'> with these indexers [boy] bu hatayı verdi
dataloc =data.loc[1:10 , "boy": "yas"]

datailoc = data.iloc[1:10 ,1 : 4].values
print("dataloc\n {} \n datailoc \n {}".format(dataloc,datailoc))


print(type(dataloc))
print(type(datailoc))


#as you can see above biri dataframe biri numpy arraya çeviriyo ... its importan ı think
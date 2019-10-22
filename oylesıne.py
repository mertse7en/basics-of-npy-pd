# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:28:06 2019

@author: Merts

new deneme
"""

data = pd.read_csv("USD_TRY Gemi Verileri.csv")
from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd        #dataframe


data.plot(kind = "scatter" , x = "Tarih" , y = "Yüksek" , alpha = 1,color = 'red' ) 
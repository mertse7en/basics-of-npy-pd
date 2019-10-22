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


data = pd.read_csv("veriler.csv")


#cok güzel bi şekilde threshhold(eşik değer) belirleyip bu eşik değere göre list comphernsıonla data ekledik dataframemize
#ortalaama yas dan farknı hesaplayan bı program ekledim

thresholdindexi = (sum(data.boy)  / len(data.boy))


data["OrtalamadanuzunMu"] = ["UZUN" if i > thresholdindexi else "KISA" for i in data.boy]
data.loc[:10,["uzunMu","boy"]] # loc'u daha sonra daha detaylı göreceğiz.

ortalamayas=28
data["ortalamadankaceksikz"] = ["sameasortalama" if i ==ortalamayas else  ortalamayas - i if i < ortalamayas else i-ortalamayas for i in data.yas ] 

#this usage of list compherasion is very important 
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:18:10 2019

@author: Merts
"""

#melt() methodu basitçe bulunan bir tablodan 
#istenilen özellikler ile yeni bir tablo oluşturulmasıdır.

from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd        #datafram
from sklearn.metrics import confusion_matrix


data = pd.read_csv("eksikveriler.csv")



newData = data.head()  # ı get first 5 sentences

#print(newData)
#yani bu napıyo kısaca özetliyim id_Vars identifier variables  oluyo (pivot değer)
#value _ vars da nonpivot olan lar
melted = pd.melt(newData , id_vars = ["boy","kilo"],value_vars = ["yas"] , var_name = "kilosu" , 
                 value_name = "bu kadardır")
print(melted)
print(type(melted))

#melt'lemenin tersi.

# Index is name
# Bu sütunların değişken olması istiyorum
# Eveet geri eski haline döndürdük =)




#veri combine etmece create 2 different dataset
data1 = data.head()
data2 = data.tail()

# axis = 0 : data setlerini satır olarak altına ekler.
# you can see what is the difference between ignore_index  false and true false kendı numaralarıyla bırakıyo
#true da ascending order lar gidi6oy

#Concatenation işlemini de <class 'pandas.core.frame.DataFrame'> bunlar uzerınden yapabılıyosun numpy .nd aray de olmuyo
#
conceted = pd.concat([data1 , data2] , axis= 0 ,ignore_index = False)  
conceted2 = pd.concat([data1 , data2] , axis= 0 ,ignore_index = True)
print(conceted)
print(conceted2)

print(type(conceted))


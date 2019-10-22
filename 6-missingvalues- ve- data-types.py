# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:18:32 2019

@author: Merts 

dropna() : drop out  the datas ,
fillna() fill the missin values,
also  eksik değerleri, ortalamayla doldururuz.

#missing values
# la nasıl başa cıkarız 
# onceliklle missin valuesi halletmek ıcın bır cok cozum var bu eyer int-
#değerlerse farklı float stringse farklı yaklaşmak gerekiyo 
#1- en besti bu altta yaptıugım #########   direk dataframe uzerınden duzeltioy
#2- imputerla çözebilrim ama dataframe i numpy.arraye çeviriyo o da uzatır işimizi concat et felan filne
#3 imputer çözümü sadi hocanın notlarda var sanırım

"""

from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd        #datafram
from sklearn.metrics import confusion_matrix


data = pd.read_csv("eksikveriler.csv")


#data.info()  as we see from info() line there are 2 missing values in yas attrs


#print(data["yas"].value_counts(dropna = False))  #again we can see  


#buda sonradan eklediğim baska bi yol fill na ile ççzüyoruz
print(data["boy"].mean())
print(data["yas"].mean())



#data["yas"].fillna(data["yas"].mean())
#data["yas"].apply(lambda x: x.fillna(x.mean()),axis=0)


data.iloc[3:5 , 2] = np.nan
#burda random bi değeri nan yaptım test ettim ful hepsını meane çeviriyomu diye iyide yaptım hepsini sadece yası degil all of u hallediyo


print(data)
data = data.groupby(data.columns, axis = 1).transform(lambda x: x.fillna(x.mean()))


#Yas=pd.DataFrame(data,columns = ["Yas"])

#imputerla yapıtgımız zaman dataframe i numpy.ndarraye çeviriyo be careful about that
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values ="NaN",strategy = "mean",axis=0)

imputer = imputer.fit(ist)
ist = imputer.transform(ist)


Yas =data.iloc[:,1:4].values

imputer = imputer.fit(Yas[:,1:4])
(Yas[:,1:4]) =imputer.transform(Yas[:,1:4])


#conceted2 = pd.concat([data1 , data2] , axis= 0 ,ignore_index = True)

# sımdı ben bunları dırek concat edemiyorum neden <class 'pandas.core.frame.DataFrame'> olması lazım tipinin
#concat etmesi için ama bizimkiler şu an numpy.ndrray ben bunu pandas df lere çeviricem


print(data)



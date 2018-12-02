#Converts gpas and gre scores to two lists of numbers of accepted and rejected \
#school ranking respectively, using keras linear regression and a functional \
#api with no hidden layer.
#Data downloaded from https://github.com/evansrjames/gradcafe-admissions-data.

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]="2"
import json
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from tensorflow.python.keras.models import Model, Sequential
from tensorflow.python.keras.layers import Input, Dense
from tensorflow.python.keras.callbacks import Callback, EarlyStopping

xx1=[4.0/4.00, 3.5/4.00]
xx2=[170/170, 150/170]
xx3=[170/170, 150/170]
xx4=[6.0/6.0, 4.5/6.0]
xx5=[990/990, 900/990]
data=np.array([xx1,xx2,xx3,xx4,xx5]).transpose()

def train(name):
    x1=[]
    x2=[]
    x3=[]
    x4=[]
    x5=[]
    y1=[]
    with open("thegradcafe_"+name+".json", "r") as nf:
        list1=json.load(nf)
    x1=np.array(list1[0])
    x2=np.array(list1[1])
    x3=np.array(list1[2])
    x4=np.array(list1[3])
    x5=np.array(list1[4])
    y1=np.array(list1[7])
    dat=np.array([x1,x2,x3,x4,x5]).transpose()
    idx_list=np.array(range(len(y1)))
    idx_test=np.random.choice(len(y1), size=int(len(y1)*0.25), replace=False)
    idx_train=np.delete(idx_list, idx_test).astype("int")
    dat_train=dat[idx_train,:]
    dat_test=dat[idx_test,:]
    y1_train=y1[idx_train]
    y1_test=y1[idx_test]
    inputs=Input(shape=(5,))
    y=Dense(1, activation="linear")
    output=y(inputs)
    model=Model(inputs, output)
    model.compile(optimizer='sgd', loss='mae', metrics=["mae"])
    history=model.fit(dat_train, y1_train, epochs=100, verbose=0)
    name=model.predict(data, verbose=1)
    print(name)

train("accepted")
train("rejected")
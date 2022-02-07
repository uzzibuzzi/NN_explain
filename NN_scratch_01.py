# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 09:27:46 2019

@author: vollmera
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 08:34:00 2019

@author: vollmera
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

from random import randrange

try:
    os.mkdir("NN2gif")
except:
    pass

dataset=np.array([[3,3,0],[3.5,0.5,0],[4,1.5,0],[5,3,0],[6,2.5,0],[5.5,2,0],[1,2,1],[1.5,3,1],[2,5,1],[3,6,1],[3,10,1]])
learningrate=0.1

def nn(m1,m2,w1,w2,b):
    z=m1*w1+m2*w2+b   
    return (z)

def sigmoid(value):
    s=1/(1+np.exp(-value))
    return (s)

abc=np.linspace(1,100)

abc=np.linspace(-10,10,100)
aaa=sigmoid(abc)
plt.scatter(abc,aaa)

def sigmoid_p(x):
    return sigmoid(x)*(1-sigmoid(x))

def tansig(n):
    return (1/(1+np.exp(-2*n)))


   
def init_nn():    
    w1=np.random.random()
    w2=np.random.random()
    b=np.random.random()
    return(w1,w2,b)

def NN_res(x,y):
    global w1,w2,b
    z=(x*w1)+(y*w2)+b
    pred=sigmoid(z)
    return pred

    
def check_error():    
    acum_er=0
    for i in dataset:
        acum_er=acum_er+(i[2]-NN_res(i[0],i[1]))**2
    return (acum_er)

def dev(target,output):
    return (target-output)*output*(1-output)
##prep diagramm
    
 
x_val=np.linspace(-10,10,100)
Y=sigmoid(x_val)
Y_d=sigmoid_p(x_val)
plt.plot(x_val,Y)
plt.plot(x_val,Y_d)
plt.show()

############################
# plot data
for i in range(len(dataset)):
    point=dataset[i]
    color="r"           #erst alles rot
    if point[2]== 0:    #nur 0 wird blau    
        color ="b"
    plt.scatter(point[0],point[1],c=color)
    plt.grid()
plt.show()
    
########       
w1,w2,b=init_nn()
print(w1,w2,b)
    
###################
# training loops 

for i in range(1 ):
    for count in range(len(dataset)):
        datawert=dataset[count]
        Z=NN_res(datawert[0],datawert[1])
        cost=np.square(Z-datawert[2])   #cost fuctio
        dcost_pred=2*(Z-datawert[2])    #ableitung cost (x²)
        dpred_dz=sigmoid_p(Z)           #ableting  sigmoid function
        dz_dw1=datawert[0]              #ableitung richutng x wird zum wert
        dz_dw2=datawert[1]              #ableitung richutng y wird zum wert
        dz_db=   1                       #ableitung bias wird zu zu1
        
        # partial derivative and chain rule in alle richutngen
        dcost_dw1=dcost_pred*dpred_dz*dz_dw1    
        dcost_dw2=dcost_pred*dpred_dz*dz_dw2
        dcost_db=dcost_pred*dpred_dz*dz_db
        
        w1=w1-(dcost_dw1*learningrate)    
        w2=w2-(dcost_dw2*learningrate) 
        b=b-(dcost_db*learningrate)        
#    if i%100==0 :                      #modulo check during training
#        print(check_error())


# daigramm for heatmap NN
X, Y, Z, = np.array([]), np.array([]), np.array([])
for ycount in range(100):  
    for xcount in range(100):
            X = np.append(X, xcount/10)
            Y = np.append(Y, ycount/10)
            Z = np.append(Z,NN_res(xcount/10,ycount/10))
plt.scatter(X,Y,c=Z,cmap="plasma")

# diagram scatter for choosen dots at the beginning
for i in range(len(dataset)):
    point=dataset[i]
    color="r"           #erst alles rot
    if point[2]== 0:    #nur 0 wird blau    
        color ="b"
    plt.scatter(point[0],point[1],c=color)
    plt.grid()
plt.savefig("NN2gif/test")
plt.show()


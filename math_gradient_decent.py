# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 08:59:32 2022

@author: vollmera
"""
import matplotlib.pyplot as plt
import numpy as np

dataset=np.array([[2,1.5,0],[4,4,0],[8.3,3.5,0]])

# plot data
for i in range(len(dataset)):
    point=dataset[i]
    color="r"           #erst alles rot
    if point[2]== 0:    #nur 0 wird blau    
        color ="b"
    plt.scatter(point[0],point[1],c=color)
    plt.grid()
plt.ylim(0,10)
plt.xlim(0,10)
    
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 08:59:32 2022

@author: vollmera
"""
import matplotlib.pyplot as plt
import numpy as np

dataset=np.array([[2,1,0],[4,4,0],[8,3,0]])

def draw_dots(dataset):# plot data
    for i in range(len(dataset)):
        point=dataset[i]
        color="r"           #erst alles rot
        if point[2]== 0:    #nur 0 wird blau    
            color ="b"
        plt.scatter(point[0],point[1],c=color)
        plt.grid()
    plt.ylim(0,10)
    plt.xlim(0,10)

def picMSE(m,dataset,i):    
    
    #Y=mx+b
    b=1
    
    x1_2 = [0, 10]
    y1_2 =  [b+m*x1_2[0], b+m*x1_2[1]]
    plt.plot(x1_2, y1_2,  c="black")
    mse=0 
    for each in range(len(dataset)):
        x1 = [dataset[each][0], dataset[each][0]]
        y1 = [dataset[each][1], b+m*dataset[each][0]]
        plt.plot(x1, y1,  c="red")
        mse+=y1[0] - y1[1]
    
#    print(mse**2) 
    plt.text(2.2, 9, "MSE {:.1f}".format(mse**2))
    draw_dots(dataset)
    plt.savefig("MSE_"+str(i)+".png")
    #plt.show()
    return mse**2
    
MSEList=[]
i=0
for every in range(10,-3,-1):
    MSEList.append(picMSE(every/10,dataset,i))
    plt.show()    
    i+=1

plt.plot(MSEList)



import imageio
images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('MSE.gif', images)
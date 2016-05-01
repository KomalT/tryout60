# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:15:45 2016

@author: sharvari
"""
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from scipy import array
from numpy import ndarray
import numpy as np
# INPUT MATRIX
Z=array([[0,0,0,0,0,0],[0,1,0,3,2,0],[0,3,2,0,1,0],[0,0,0,2,0,0],[0,2,1,0,3,0],[0,0,0,0,0,0]])
size=len(Z),len(Z[0])
print size
N = np.zeros(np.shape(Z))
# initialisation
a=b=c=d=0 
count=[]
t1=[]
#fragmentation
def new(Z):
    for i in range(4):
        for j in range(4):
            K=Z[i:(i+3),j:(j+3)]
            a=0;b=0;c=0;d=0;
            for l in range(3):
                for m in range(3):
                
                    
                        if l!=1 or m!=1:
                            if K[l,m]==0:
                                a=a+1
                            elif K[l,m]==1:
                                b=b+1
                            elif K[l,m]==2:
                                c=c+1
                            elif K[l,m]==3:
                                d=d+1
                            e=K[1,1]
                        K=([a,b,c,d,e]) 
                        print K
        
        count.append(K)
        
    for i in range(16):
        K=count[i]
        a=K[0];b=K[1];c=K[2];d=K[3];e=K[4]
        if e==0:
            if b>0:
                e=1
        if e==2:
            if b<2:
                e=0
        if e==0:
            if b>=2 and c>=1:
                e=2
        if e==1:
            if c>1:
                e=0
        if e==1:
            if c>2 and d>=1:
                e=3
        
        K[4]=e
        print K
        return(Z)
plt.imshow(Z)
#plt.colorbar() 
plt.pause(5)
Z1=new(Z)
print Z1
plt.imshow(Z1)
#plt.colorbar() 
plt.pause(5)
Z2=new(Z1)
print Z2
plt.imshow(Z2)
#plt.colorbar() 
plt.pause(5)
Z3=new(Z2)
print Z3
plt.imshow(Z3)


     


    
    

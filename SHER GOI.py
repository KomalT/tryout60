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
#Z=array([[0,0,0,0,0,0],[0,1,3,1,2,0],[0,1,2,1,1,0],[0,1,3,2,1,0],[0,2,1,2,3,0],[0,0,0,0,0,0]])
Z = np.random.randint(0,4,size=(6,6))
size=len(Z),len(Z[0])
#print size
plt.imshow(Z)
#plt.colorbar() 
plt.pause(2) 
N = np.zeros(np.shape(Z))
# initialisation
a1=b1=c1=d1=0 
count=[]
t1=[]
new=[]
#fragmentation
#def new(Z):
new1=Z[1:5,1:5]
for i in range(3):
    Z[1:5,1:5]=new1 
    for i in range(4):
        for j in range(4):
            K1=Z[i:(i+3),j:(j+3)]
            
            for l in range(3):
                for m in range(3):
                    a1=0;b1=0;c1=0;d1=0;
                    
                    if l!=1 or m!=1:
                        if K1[l,m]==0:
                            a1=a1+1
                        elif K1[l,m]==1:
                            b1=b1+1
                        elif K1[l,m]==2:
                            c1=c1+1
                        elif K1[l,m]==3:
                            d1=d1+1
                        e=K1[1,1]
                        K2=([a1,b1,c1,d1,e]) 
                        #print K
        
                        count.append(K2)
    #print count        
               
    for i in range(16):
        K=count[i]
        #print K
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
    
        new.append(e)
    
    new1=np.reshape(new, (4, 4))
    #print new1
    Z[1:5,1:5]=new1
    #print Z
    t1.append(new1)
    count=[]
    new=[]
print t1
tr=np.reshape(t1,(12,4))
KA=tr[0:4,:]
Z[1:5,1:5]=KA
#print Z
plt.imshow(Z)
#plt.colorbar() 
plt.pause(2)
KB=tr[4:8,:]
Z[1:5,1:5]=KB
#print Z 
plt.imshow(Z)
#plt.colorbar() 
plt.pause(2)   
KC=tr[8:12,:]
Z[1:5,1:5]=KC
#print Z
plt.imshow(Z)
#plt.colorbar() 
plt.pause(2)

     


    
    

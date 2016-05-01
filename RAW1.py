# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:35:04 2016

@author: user
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:15:45 2016

@author: KT
"""
from scipy import array
from numpy import ndarray
import numpy as np
from numpy import reshape
import matplotlib.animation as animation
import matplotlib.pyplot as plt

# INPUT MATRIX
Z=array([[0,0,0,0,0,0],[0,2,1,2,3,0],[0,3,2,1,2,0],[0,3,1,2,3,0],[0,2,1,3,1,0],[0,0,0,0,0,0]])
#print Z
#plt.imshow(Z)
#plt.show()
size=len(Z),len(Z[0])
#print size
t1=[]
# COUNTING
def count(Z):
    size=len(Z),len(Z[0])
    a=0;b=0;c=0;d=0;
    for i in range(0,size[0]):
        for j in range(0,size[1]):
            if i!=1 or j!=1:
                if Z[i,j]==0:
                    a=a+1
                elif Z[i,j]==1:
                    b=b+1
                elif Z[i,j]==2:
                    c=c+1
                elif Z[i,j]==3:
                    d=d+1
                e=Z[1,1]
    return array([a,b,c,d,e])

# MODIFICATION
def modi(k):
    a=k[0];b=k[1];c=k[2];d=k[3];e=k[4]
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
    return e 
def update(Z):
    
    Z11=Z[:-3,:-3]   
    k11=count(Z11)
    e11=modi(k11)
    
    Z12=Z[:-3,1:-2]
    k12=count(Z12)
    e12=modi(k12)
    

    Z13=Z[:-3,2:-1]
    k13=count(Z13)
    e13=modi(k13)
    

    Z14=Z[:-3,3:]
    k14=count(Z14)
    e14=modi(k14)
    

    Z21=Z[1:-2,:-3]
    k21=count(Z21)
    e21=modi(k21)
    

    Z22=Z[1:-2,1:-2]
    k22=count(Z22)
    e22=modi(k22)
    

    Z23=Z[1:-2,2:-1]
    k23=count(Z23)
    e23=modi(k23)
    

    Z24=Z[1:-2,3:]
    k24=count(Z24)
    e24=modi(k24)
    

    Z31=Z[2:-1,:-3]
    k31=count(Z31)
    e31=modi(k31)
    

    Z32=Z[2:-1,1:-2]
    k32=count(Z32)
    e32=modi(k32)
    

    Z33=Z[2:-1,2:-1]
    k33=count(Z33)
    e33=modi(k33)
    

    Z34=Z[2:-1,3:]
    k34=count(Z34)
    e34=modi(k34)
    

    Z41=Z[3:,:-3]
    k41=count(Z41)
    e41=modi(k41)
    

    Z42=Z[3:,1:-2]
    k42=count(Z42)
    e42=modi(k42)
    

    Z43=Z[3:,2:-1]
    k43=count(Z43)
    e43=modi(k43)
    

    Z44=Z[3:,3:]
    k44=count(Z44)
    e44=modi(k44)
    
    
    Z[1,1]=e11
    Z[1,2]=e12
    Z[1,3]=e13
    Z[1,4]=e14
    Z[2,1]=e21
    Z[2,2]=e22
    Z[2,3]=e23
    Z[2,4]=e24
    Z[3,1]=e31
    Z[3,2]=e32
    Z[3,3]=e33
    Z[3,4]=e34
    Z[4,1]=e41
    Z[4,2]=e42
    Z[4,3]=e43
    Z[4,4]=e44
    return Z
    #print Z
    #fig=plt.figure()
    #ax=fig.add_subplot(111)
    #t=plt.imshow(Z)
    #t1.append([t])
    #plt.colorbar() 
    #plt.pause(5)
    #plt.show()
    #fig, ax = plt.subplots()
    #mat = ax.matshow(Z)
    #ani = animation.FuncAnimation(fig, update, interval=50,
                              #save_count=50)
#plt.show()
#ani = animation.ArtistAnimation(fig, t1, interval=50, blit=True,
                                #repeat_delay=1000)
#ani.save('dynamic_images.mp4')
#plt.show()
Z=array([[0,0,0,0,0,0],[0,2,1,2,3,0],[0,3,3,1,2,0],[0,3,1,2,3,0],[0,2,1,3,1,0],[0,0,0,0,0,0]])
print Z
plt.imshow(Z)
#plt.colorbar() 
plt.pause(5)
Z1=update(Z)
print Z1
plt.imshow(Z1)
#plt.colorbar() 
plt.pause(5)
Z2=update(Z1)
print Z2
plt.imshow(Z2)
#plt.colorbar() 
plt.pause(5)
Z3=update(Z2)
print Z3
plt.imshow(Z3)
#plt.colorbar() 
#plt.pause(5)
#plt.imshow(Z1)
#plt.colorbar() 
#plt.pause(5)
#plt.imshow(Z2)
#plt.colorbar() 
#plt.pause(5)
#plt.imshow(Z3)
#plt.colorbar() 
Z=array([[0,0,0,0,0,0],[0,2,1,2,3,0],[0,3,2,1,2,0],[0,3,1,2,3,0],[0,2,1,3,1,0],[0,0,0,0,0,0]])

#for i in range(4):
    #print Z
    #fig=plt.figure()
    #ax=fig.add_subplot(212)
    #plt.imshow(Z)
    #t1.append([t])
    #plt.colorbar()
    #Z=update(Z)
    #plt.pause(.1)
#plt.show()
#fig,ax=plt.subplots()
#mat=ax.matshow(Z)
#ani = animation.FuncAnimation(fig, update, interval=50, save_count=50)
#ani.save('dynamic_images.mp4')
#plt.pause(.1)
#plt.show()


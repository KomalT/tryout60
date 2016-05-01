# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:15:45 2016

@author: KT
"""
from scipy import array
from numpy import ndarray
import numpy as np
from numpy import reshape
e=[0,0,0,0,0,0,0]
# INPUT MATRIX
Z=array([[0,0,0,0,0,0],[0,1,0,3,2,0],[0,3,2,0,1,0],[0,0,0,2,0,0],[0,2,1,0,3,0],[0,0,0,0,0,0]])
#print Z
size=len(Z),len(Z[0])
#print size

# initialisation
a=np.zeros((4,4),int) # COUNTER FOR 0
#print a

b=np.zeros((4,4),int) # COUNTER FOR 1
#print b

c=np.zeros((4,4),int) # COUNTER FOR 2
#print c

d=np.zeros((4,4),int) # COUNTER FOR 3
#print d

# fragmentation
Z11=Z[:-3,:-3]
#print Z11

Z12=Z[:-3,1:-2]
#print Z12

Z13=Z[:-3,2:-1]
#print Z13

Z14=Z[:-3,3:]
#print Z14

Z21=Z[1:-2,:-3]
#print Z21

Z22=Z[1:-2,1:-2]
#print Z22

Z23=Z[1:-2,2:-1]
#print Z23

Z24=Z[1:-2,3:]
#print Z24

Z31=Z[2:-1,:-3]
#print Z31

Z32=Z[2:-1,1:-2]
#print Z32

Z33=Z[2:-1,2:-1]
#print Z33

Z34=Z[2:-1,3:]
#print Z34

Z41=Z[3:,:-3]
#print Z41

Z42=Z[3:,1:-2]
#print Z42

Z43=Z[3:,2:-1]
#print Z43

Z44=Z[3:,3:]
#print Z44

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
    
k11=count(Z11)
#print k11
e=e+[modi(k11)]
print e

k12=count(Z12)
#print k12
e12=(modi(k12))
#print e

k13=count(Z13)
#print k13
e13=(modi(k13))

k14=count(Z14)
#print k14
e14=(modi(k14))

#e.append(0)
#e.append(0)
k21=count(Z21)
#print k21
e21=(modi(k21))

k22=count(Z22)
#print k22
e22=(modi(k22))

k23=count(Z23)
#print k21
e23=(modi(k23))

k24=count(Z24)
#print k21
e24=(modi(k24))

#e.append(0)
#e.append(0)

k31=count(Z31)
#print k21
e31=(modi(k31))

k32=count(Z32)
#print k21
e32=(modi(k32))

k33=count(Z33)
#print k21
e33=(modi(k33))

k34=count(Z34)
#print k21
e34=(modi(k34))

#e.append(0)
#e.append(0)

k41=count(Z41)
#print k21
e41=(modi(k41))

k42=count(Z42)
#print k21
e42=(modi(k42))

k43=count(Z43)
#print k21
e43=(modi(k43))

k44=count(Z44)
#print k21
e44=(modi(k44))
#e.append(0)
#e.append(0)
#e.append(0)
#e.append(0)
#e.append(0)
#e.append(0)
#e.append(0)
#shape1=(6,6)
#e.reshape(shape1)
#b=e.reshape(6,6)
#print b
#A=array([0,0,0,0,0,0],[0,e11,e12,e13,e14,0],[0,e21,e22,e23,e24,0],[0,e31,e32,e33,e34,0],[0,e41,e42,e43,e44,0],[0,0,0,0,0,0])
#print A
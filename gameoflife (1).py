# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 10:33:34 2016

@author: Ankit
"""

import scipy
from scipy import array
import numpy as np
a=np.array([[0,0,0,0],[0,1,2,0],[0,0,1,0],[0,0,0,0]])
print a
print a.shape
shape=len(a),len(a[0])
def barearth(x,y):   # x=grass, y= prey
    if x>=2  and y>=1:
        z=2
    if x>0:
        z=1
    else:
        z=0
    
    return z
def grass(x):  # x=prey
    if x>1:
        z=0
    else:
        z=1
    return z
def prey(x):  #x=grass
    if x<1:
        z=0
    if x>2:
        z=2
    else:
        z=1
    return z
for v in range(3):
    
    for m in range(1,shape[0]-1):
        for n in range(1,shape[1]-1):
            z=a[m,n]
            print (z)
            gr=0;pr=0;pred=0;
            b=array([a[m-1,n-1],a[m-1,n],a[n-1,n],a[m,n-1],a[m,n+1],a[m+1,n-1],a[m+1,n],a[m+1,n+1]])
            for l in range(8):
                if b[l]==1:
                    gr=gr+1;
                if b[l]==2:
                    pr=pr+1;
                #if b[l]==3:
                    #pred=pred+1
            if z==0:
                a[m,n]=barearth(gr,pr);
            if z==1:
                a[m,n]=grass(pr);
            if z==2:
                a[m,n]=prey(gr);
            #if z==3:
                  #a[m,n]=predator(pr);
        print (a)
               


    
    
        
    
    
        
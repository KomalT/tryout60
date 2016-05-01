# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 22:47:15 2016

@author: user
"""
import scipy,scipy.optimize
import matplotlib.pyplot as plt
import numpy as np
from scipy import array
Le=2.52  # m empty pipe
Lm=2.69  # m with mixing element
De=.0209 # m empty
Dm=.0198 # m with mixing element
Row=1000 # Kg/m3
RoHg=13600 #Kg/m3
RoC=1487 # Kg/m3
Meu=0.001 # Pa.s
DelRo=1   # Kg/m3
DelH=0.001# m
DelD=2*10**(-5)#m
DelL=0.002# m
DelQ=0.002# m
Q=array([19.104*10**-6,27.3*10**-6,32*10**-6,57.85*10**-6,70.87*10**-6,87.88*10**-6])
H=array([0.5*10**-2,1*10**-2,1.1*10**-2,1.8*10**-2,2.5*10**-2,3.5*10**-2])
x=array([1164.42,1663.97,1950.45,3526.04,4319.63,5356.41])
y=array([.03188,.03122,.025,.0125,.01158,.01055])
constant=(2*(DelRo/(RoC-Row))**2)+((DelRo/Row)**2)+((DelL/Le)**2)+(5*DelD/De)**2
ErrbyY=(9.81*8/3.14**2)*np.sqrt(constant+(DelH**2)/np.square(H)+((2*DelQ)**2)/np.square(Q))
yerr=np.multiply(y,ErrbyY)

def curve(x,p):
    [A,B]=p
    y=A*x**B
    return y
def err1(p,x,y,yerr):
    err=(y-curve(x,p))/yerr
    return err
def get_r2(x,y,ycalc):
    ymean=scipy.average(y)
    dymean2=(y-ymean)**2
    dycalc2=(y-ycalc)**2
    r2=1-sum(dycalc2)/sum(dymean2)
    return r2
pguess=[16,-1]
res=scipy.optimize.leastsq(err1,pguess,args=(x,y,yerr))
P=res[0]
print P
ycalc=curve(x,P)
r2=get_r2(x,y,ycalc)
fig=plt.figure();
ax=fig.add_subplot(111)
ax.plot(x,y,'*')
ax.plot(x,ycalc,'b')    
ax.title.set_text('R2=%f'%(r2))
fig.canvas.draw()
plt.show()  

    
    
    
    
    
    
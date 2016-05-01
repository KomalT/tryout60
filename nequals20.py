# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 21:35:23 2016

@author: stu
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 09 23:36:50 2016

@author: user
"""
from scipy.integrate import odeint
from scipy import linspace
from scipy import array
import numpy as np
#import matplotlib.pyplot as plt
kla=0.07
A=2*10**(-2)
pT=1#"""atm"""
Hc=29.4#"""atm/M"""
MDc=4.089*10**(-2)#"M"
Hm=714.286#"atm/M"
MDm=4.1*10**(-2)#"M"
kGa=0.07
Pwsat=0.03#"atm"
def derivate(y,t):
    yc=y[0]/(y[0]+y[1]+y[2])
    ym=y[1]/(y[0]+y[1]+y[2])
    yw=y[2]/(y[0]+y[1]+y[2])
    xc=y[3]/(y[3]+y[4]+y[5])
    xm=y[4]/(y[3]+y[4]+y[5])
    #xw=y[5]/(y[3]+y[4]+y[5])
    dGc=-kla*A*(yc*pT/Hc-MDc*xc)
    dLc=-kla*A*(yc*pT/Hc-MDc*xc)
    dGm=-kla*A*(ym*pT/Hm-MDm*xm)
    dLm=-kla*A*(ym*pT/Hm-MDm*xm)
    dGw=kGa*A*(pT*yw-Pwsat)
    dLw=kGa*A*(pT*yw-Pwsat)
    return array([dGc,dLc,dGm,dLm,dGw,dLw])

#def guess(a):
    #return array([a1,a2,a3])
def additive(e,a):
    if e[0]>0.1:
        a[0]=a[0]+0.001
    if e[1]>0.1:
        a[1]=a[1]+0.001
    if e[2]>0.1:
        a[2]=a[2]-0.001
    return ([a[0],a[1],a[2]])   
a1=0;a2=0;a3=100
t=linspace(0.0,2.0,20)
#print t
yinitial=([50,50,0,a1,a2,a3])
y=odeint(derivate,yinitial,t)
#print y
def error(y):
    e1=100-y[19,5]#"liq water"
    e2=y[19,4]#"liq CH4"
    e3=y[19,3]#"liq CO2"
    return array([e1,e2,e3])
e11=error(y)
if e11[0]<0:
    e11[0]=-e11[0]
if e11[1]<0:
    e11[1]=-e11[1]
if e11[2]<0:
    e11[2]=-e11[2]

    #err=max(e13[0],e13[1],e13[2])
#print e11
a11= array([a1,a2,a3])
#print a11
a1=.5;a2=.5;a3=90
t=linspace(0.0,2.0,20)
yinitial=([50,50,0,a1,a2,a3])
y=odeint(derivate,yinitial,t)
e12=error(y)
if e12[0]<0:
    e12[0]=-e12[0]
if e12[1]<0:
    e12[1]=-e12[1]
if e12[2]<0:
    e12[2]=-e12[2]
    #err=max(e13[0],e13[1],e13[2])
#print e12
a12= array([a1,a2,a3])
#print a12
k1=[]
a13=[]
err=1
while (err>.05):
    #k1=np.multiply((a12-a11),e12)
    a13=additive(e11,a11)
    t=linspace(0.0,2.0,20)
    yinitial=([50,50,0,a13[0],a13[1],a13[2]])
    y=odeint(derivate,yinitial,t)
    e13=error(y)
    if e13[0]<0:
        e13[0]=-e13[0]
    if e13[1]<0:
        e13[1]=-e13[1]
    if e13[2]<0:
        e13[2]=-e13[2]
    err=max(e13[0],e13[1],e13[2])
    a11=a13
    e11=e13
    #ans=a2
    #if e13[0]<0:
       #e13[0]=-e13[0]
    #e11=e12
    #e12=e13
    #a11=a12
    #a12=a13
    print err
    #if k < 0:
        #k= -1 * k
    #err=k  
print y[9,5]
print y[9,4]
print y[9,3]
print y[9,2]
print y[9,1]
print y[9,0]
#print a13
error1=200-(y[19,5]+ y[19,4]+ y[19,3]+ y[19,2]+ y[19,1]+ y[19,0])
print error1
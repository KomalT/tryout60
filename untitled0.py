# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 17:05:31 2016

@author: user
"""
from scipy.integrate import odeint
from scipy import linspace
from scipy import array
import numpy
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
kla=0.004
A=10
pT=1#"""atm"""
Hc=29.4#"""atm/M"""
MDc=4.089*10**(-2)#"M"
Hm=714.286#"atm/M"
MDm=4.1*10**(-2)#"M"
kGa=0.0002
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
a=array ([50,50,0])
t=linspace(0.0,10.0,100)
#yinitial=([50,50,0,a1,a2,a3])
#y=odeint(derivate,yinitial,t)
#print y[9,5]
def error(a):
    t=linspace(0.0,10.0,100)
    yinitial=([a[0],a[1],a[2],a[0],a[1],a[2]])
    y=odeint(derivate,yinitial,t)
    return array([y[99,5]-100,y[99,4],y[99,3]])
ans=fsolve(error,a)
print ans
yinitial=([50,50,0,ans[0],ans[1],ans[2]])
y=odeint(derivate,yinitial,t)
print y[99,:]
#plt.plot(t,)
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 20:52:50 2016

@author: user
"""
from scipy.integrate import odeint
from scipy import linspace
from scipy import array
import numpy
kla=0.07#sec-1
A=2*10**(-2)#m2
pT=1#"""atm"""
Hc=29.4#"""atm/M"""
MDc=4.089*10**(-2)#"M"
Hm=714.286#"atm/M"
MDm=4.1*10**(-2)#"M"
kGa=0.07
Pwsat=0.3#"atm"
def deri(y,t):
     xc=y[0]/(y[0]+y[1]+y[2])
     xm=y[1]/(y[0]+y[1]+y[2])
     xw=y[2]/(y[0]+y[1]+y[2])
     yc=(50-y[0])/(200-(y[0]+y[1]+y[2]))
     ym=(50-y[1])/(200-(y[0]+y[1]+y[2]))
     yw=(100-y[2])/(200-(y[0]+y[1]+y[2]))
     dLcdz=kla*A*(yc*pT/Hc-MDc*xc)
     dLmdz=kla*A*(ym*pT/Hm-MDm*xm)
     dLwdz=kGa*A*(pT*yw-Pwsat)
     return array([dLcdz,dLmdz,dLwdz])
t=linspace(0.0,2.0,10)
yinitial=([0,0,100])
y=odeint(deri,yinitial,t)
print y[9,2]
print y[9,1]
print y[9,0]
Gc=50-y[9,0]
Gm=50-y[9,1]
Gw=100-y[9,2]
print Gc
print Gm
print Gw

t=linspace(0.0,2.0,30)
yinitial=([0,0,100])
y=odeint(deri,yinitial,t)
print y[29,2]
print y[29,1]
print y[29,0]
Gc=50-y[29,0]
Gm=50-y[29,1]
Gw=100-y[29,2]
print Gc
print Gm
print Gw

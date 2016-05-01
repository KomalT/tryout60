# -*- coding: utf-8 -*-
"""
Created on Sat Jan 09 17:15:22 2016

@author: user
"""
from scipy.integrate import odeint
from scipy import linspace
from scipy import array
import numpy
import matplotlib.pyplot as plt
kla=1
A=2
pT=1#"""atm"""
Hc=29.4#"""atm/M"""
MDc=4.089*10**(-2)#"M"
Hm=714.286#"atm/M"
MDm=4.1*10**(-2)#"M"
kGa=2
Pwsat=0.03#"atm"
def derivate(y,t):
    yc=y[0]/(y[0]+y[1]+y[2])
    ym=y[1]/(y[0]+y[1]+y[2])
    yw=y[2]/(y[0]+y[1]+y[2])
    xc=y[3]/(y[3]+y[4]+y[5])
    xm=y[4]/(y[3]+y[4]+y[5])
    xw=y[5]/(y[3]+y[4]+y[5])
    dGc=-kla*A*(yc*pT/Hc-MDc*xc)
    dLc=-kla*A*(yc*pT/Hc-MDc*xc)
    dGm=-kla*A*(ym*pT/Hm-MDm*xm)
    dLm=-kla*A*(ym*pT/Hm-MDm*xm)
    dGw=kGa*A*(pT*yw-Pwsat)
    dLw=kGa*A*(pT*yw-Pwsat)
    return array([dGc,dLc,dGm,dLm,dGw,dLw])
n=[11,21,31,51,71,101]
n1=[10,20,30,50,70,100]
percent_error=[]
def error(e,y):
    e1=100-y[n1[i],5]#"liq water"
    e2=y[n1[i],4]#"liq CH4"
    e3=y[n1[i],3]#"liq CO2"
    return array([e1,e2,e3])
m1=0.001;m2=0.001;m3=0.001
for i in range(6):
    a1=0;a2=0;a3=100
    e1=100;e2=100;e3=100
    mxm=100
    while(mxm>0.1):
        if e1 > 0.1:
            a1=a1+m1
        if e2 > 0.1:
            a2=a2+m2
        if e3 >0.1:
            a3=a3-m3
        t=linspace(0.0,2.0,n[i])
        yinitial=([50,50,0,a1,a2,a3])
        y=odeint(derivate,yinitial,t)
        print y[n1[i],3]
        print y[n1[i],4]
        print y[n1[i],5]
        e1=100-y[n1[i],5]#"liq water"
        if e1 < 0:
            e1=-e1
        e2=y[n1[i],4]#"liq CH4"
        if e2 < 0:
            e2=-e2
        e3=y[n1[i],3]#"liq CO2"
        if e3 < 0:
            e3=-e3
        mxm=e1
        if e2>mxm:
            mxm=e2
        if e3>mxm:
            mxm=e3
    #print y[n1[i],3]
    #print y[n1[i],4]
    #print y[n1[i],5]
    
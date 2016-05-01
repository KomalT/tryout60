# -*- coding: utf-8 -*-
"""
Created on Sat Jan 02 23:03:54 2016

@author: user
"""

from scipy.integrate import odeint
from scipy import linspace
from scipy import array
import numpy
import matplotlib.pyplot as plt
def deriv(y,t):
    U=100
    P=1
    mA=1
    mB=2
    cPA=4000+10*y[0]+10**(-2)*y[0]**2
    cPB=3000+5*y[1]+2*10**(-2)*y[1]**2
    return array([-U*P/(mA*(cPA))*(y[0]-y[1]) , -U*P/(mB*(cPB))*(y[0]-y[1])])
a1=309
t=linspace(0.0,9.0,10)
yinitial=([400,a1])
y=odeint(deriv,yinitial,t)
F1=y[9,1]-300
print F1

a2=308
t=linspace(0.0,10.0,11)
yinitial=([400,a2])
y=odeint(deriv,yinitial,t)
F2=y[10,1]-300
print F2
err=1
while (err>0.00000001):  
    a3=a2-(a2-a1)*F2/(F2-F1)
    t=linspace(0.0,10.0,11)
    yinitial=([400,a3])
    y=odeint(deriv,yinitial,t)
    F3=y[10,1]-300
    ans=a2
    F1=F2
    F2=F3
    a1=a2
    a2=a3
    k=y[10,1]-300
    if k < 0:
        k= -1 * k
    err=k  
print ans # TB0
print y[10,0] #TA(n-1)
Qa=1*(4000*(400-y[10,0])+5*(400**2-(y[10,0])**2)+10**(-2)/3*(400**3-(y[10,0])**3))
Qb=-2*(3000*(300-ans)+2.5*(300**2-(ans)**2)+2*10**(-2)/3*(300**3-(ans)**3))
print Qa
print Qb
percent_error=(Qb-Qa)/Qa*100
print percent_error
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 03 11:11:12 2016

@author: user
"""

from scipy.integrate import odeint
from scipy import linspace
from scipy import array
import numpy
def deriv(y,t):
    U=100
    P=1
    mA=1
    mB=2
    ##cPA=4000+10*y(1)+10**(-2)*y(1)**2
    ##cPB=3000+5*y(2)+2*10**(-2)*y(2)**2
    return array([-U*P/(mA*(4000+10*y[0]+10**(-2)*y[0]**2))*(y[0]-y[1]) , -U*P/(mB*(3000+5*y[1]+2*10**(-2)*y[1]**2))*(y[0]-y[1])])
n=array([10,20,30,40,50,70,100])
n1=array([9,19,29,39,49,69,99])
for i in range(7):
    a1=310
    q1=n[i]
    t=linspace(0.0,9.0,q1)
    yinitial=([400,a1])
    y=odeint(deriv,yinitial,t)
    F1=y[n1[i],1]-300
    print F1

    a2=320
    t=linspace(0.0,9.0,n[i])
    yinitial=([400,a2])
    y=odeint(deriv,yinitial,t)
    F2=y[n1[i],1]-300
    print F2
    err=1
    while (err>0.01):  
        a3=a2-((a2-a1)/(F2-F1))*F2
        t=linspace(0.0,9.0,n[i])
        yinitial=([400,a3])
        y=odeint(deriv,yinitial,t)
        F3=y[n1[i],1]-300
        ans=a2
        F1=F2
        F2=F3
        a1=a2
        a2=a3
        k=y[n1[i],1]-300
        if k < 0:
            k= -1 * k
            err=k  
    print a2 # TB0
    print y[n1[i],0] #TA(n-1)
print ans[0:6]
print ans2[0:6]
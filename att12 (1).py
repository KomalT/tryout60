# -*- coding: utf-8 -*-
"""
Created on Mon Jan 04 21:43:11 2016

@author: stu
"""
from scipy.integrate import odeint
from scipy import linspace
from scipy import array
import numpy
from pylab import *
from scipy.integrate import quad
def deriv(y,t):
    U=100
    P=1
    mA=1
    mB=2
    ##cPA=4000+10*y(1)+10**(-2)*y(1)**2
    ##cPB=3000+5*y(2)+2*10**(-2)*y(2)**2
    return array([-U*P/(mA*(4000+10*y[0]+10**(-2)*y[0]**2))*(y[0]-y[1]) , -U*P/(mB*(3000+5*y[1]+2*10**(-2)*y[1]**2))*(y[0]-y[1])])
n=[11,21,31,51,71,101]
n1=[10,20,30,50,70,100]
percent_error=[]
for i in range(6):
### FOR N=10
    a1=310
    t=linspace(0.0,10.0,n[i])
    yinitial=([400,a1])
    y=odeint(deriv,yinitial,t)
    F1=y[n1[i],1]-300
    #print F1

    a2=315
    t=linspace(0.0,10.0,n[i])
    yinitial=([400,a2])
    y=odeint(deriv,yinitial,t)
    F2=y[n1[i],1]-300
    #print F2
    err=1
    while (err>0.00000001):  
        a3=a2-(a2-a1)*F2/(F2-F1)
        t=linspace(0.0,10.0,n[i])
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
            #print ans # TB0
            #print y[n1[i],0] #TA(n-1)
#Qa=1*(4000*(400-y[9,0])+5*(400**2-(y[9,0])**2)+10**(-2)/3*(400**3-(y[9,0])**3))
#Qb=-2*(3000*(300-ans)+2.5*(300**2-(ans)**2)+2*10**(-2)/3*(300**3-(ans)**3))
    def qA(T):
        return 4000+10*T+10**(-2)*T**2
    [Qa,err]=quad(qA,y[n1[i],0],400)
    print Qa

    def qB(T):
        return -2*(3000+5*T+2*10**(-2)*T**2)
    [Qb,err]=quad(qB,ans,300)
    print Qb
#Qa1=Qa[0,0]
#Qb1=Qb[0,0]
#print Qa
#print Qb
    percent_error.append((Qb-Qa)/Qa*100)
print percent_error


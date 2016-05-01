# -*- coding: utf-8 -*-
"""
Created on Sun Jan 03 13:20:49 2016

@author: user
"""
from scipy.integrate import odeint
from scipy import linspace
from scipy import array
import numpy
from pylab import *
from scipy.integrate import quad
import matplotlib.pyplot as plt
def deriv(y,t):
    U=100
    P=1
    mA=1
    mB=2
    ##cPA=4000+10*y(1)+10**(-2)*y(1)**2
    ##cPB=3000+5*y(2)+2*10**(-2)*y(2)**2
    return array([-U*P/(mA*(4000+10*y[0]+10**(-2)*y[0]**2))*(y[0]-y[1]) , -U*P/(mB*(3000+5*y[1]+2*10**(-2)*y[1]**2))*(y[0]-y[1])])

### FOR N=10
a1=307
t=linspace(0.0,9.0,10)
yinitial=([400,a1])
y=odeint(deriv,yinitial,t)
F1=y[9,1]-300
#print F1

a2=308
t=linspace(0.0,9.0,10)
yinitial=([400,a2])
y=odeint(deriv,yinitial,t)
F2=y[9,1]-300
#print F2
err=1
while (err>0.00000001):  
    a3=a2-(a2-a1)*F2/(F2-F1)
    t=linspace(0.0,9.0,10)
    yinitial=([400,a3])
    y=odeint(deriv,yinitial,t)
    F3=y[9,1]-300
    ans=a2
    F1=F2
    F2=F3
    a1=a2
    a2=a3
    k=y[9,1]-300
    if k < 0:
        k= -1 * k
    err=k  
#print ans # TB0
#print y[9,0] #TA(n-1)
#Qa=1*(4000*(400-y[9,0])+5*(400**2-(y[9,0])**2)+10**(-2)/3*(400**3-(y[9,0])**3))
#Qb=-2*(3000*(300-ans)+2.5*(300**2-(ans)**2)+2*10**(-2)/3*(300**3-(ans)**3))
def qA(T):
    return 4000+10*T+10**(-2)*T**2
[Qa,err]=quad(qA,y[9,0],400)
#print Qa

def qB(T):
    return -2*(3000+5*T+2*10**(-2)*T**2)
[Qb,err]=quad(qB,ans,300)
#print Qb
#Qa1=Qa[0,0]
#Qb1=Qb[0,0]
#print Qa
#print Qb
percent_error1=(Qb-Qa)/Qa*100
print percent_error1


n=20
a1=307
t=linspace(0.0,9.0,20)
yinitial=([400,a1])
y=odeint(deriv,yinitial,t)
F1=y[19,1]-300
#print F1

a2=308
t=linspace(0.0,9.0,20)
yinitial=([400,a2])
y=odeint(deriv,yinitial,t)
F2=y[19,1]-300
#print F2
err=1
while (err>0.00000001):  
    a3=a2-(a2-a1)*F2/(F2-F1)
    t=linspace(0.0,9.0,20)
    yinitial=([400,a3])
    y=odeint(deriv,yinitial,t)
    F3=y[19,1]-300
    ans=a2
    F1=F2
    F2=F3
    a1=a2
    a2=a3
    k=y[19,1]-300
    if k < 0:
        k= -1 * k
    err=k  
#print ans # TB0
#print y[19,0] #TA(n-1)
#Qa=1*(4000*(400-y[19,0])+5*(400**2-(y[19,0])**2)+10**(-2)/3*(400**3-(y[19,0])**3))
#Qb=-2*(3000*(300-ans)+2.5*(300**2-(ans)**2)+2*10**(-2)/3*(300**3-(ans)**3))
#print Qa
#print Qb
def qA(T):
    return 4000+10*T+10**(-2)*T**2
[Qa,err]=quad(qA,y[19,0],400)
#print Qa

def qB(T):
    return -2*(3000+5*T+2*10**(-2)*T**2)
[Qb,err]=quad(qB,ans,300)
#print Qb

percent_error2=(Qb-Qa)/Qa*100
print percent_error2


n=30
a1=307
t=linspace(0.0,9.0,30)
yinitial=([400,a1])
y=odeint(deriv,yinitial,t)
F1=y[29,1]-300
#print F1

a2=308
t=linspace(0.0,9.0,30)
yinitial=([400,a2])
y=odeint(deriv,yinitial,t)
F2=y[29,1]-300
#print F2
err=1
while (err>0.00000001):  
    a3=a2-(a2-a1)*F2/(F2-F1)
    t=linspace(0.0,9.0,30)
    yinitial=([400,a3])
    y=odeint(deriv,yinitial,t)
    F3=y[29,1]-300
    ans=a2
    F1=F2
    F2=F3
    a1=a2
    a2=a3
    k=y[29,1]-300
    if k < 0:
        k= -1 * k
    err=k  
#print ans # TB0
#print y[29,0] #TA(n-1)
#Qa=1*(4000*(400-y[29,0])+5*(400**2-(y[29,0])**2)+10**(-2)/3*(400**3-(y[29,0])**3))
#Qb=-2*(3000*(300-ans)+2.5*(300**2-(ans)**2)+2*10**(-2)/3*(300**3-(ans)**3))
#print Qa
#print Qb
def qA(T):
    return 4000+10*T+10**(-2)*T**2
[Qa,err]=quad(qA,y[29,0],400)
#print Qa

def qB(T):
    return -2*(3000+5*T+2*10**(-2)*T**2)
[Qb,err]=quad(qB,ans,300)
#print Qb

percent_error3=(Qb-Qa)/Qa*100
print percent_error3

n=50
a1=307
t=linspace(0.0,9.0,50)
yinitial=([400,a1])
y=odeint(deriv,yinitial,t)
F1=y[49,1]-300
#print F1

a2=308
t=linspace(0.0,9.0,50)
yinitial=([400,a2])
y=odeint(deriv,yinitial,t)
F2=y[49,1]-300
#print F2
err=1
while (err>0.00000001):  
    a3=a2-(a2-a1)*F2/(F2-F1)
    t=linspace(0.0,9.0,50)
    yinitial=([400,a3])
    y=odeint(deriv,yinitial,t)
    F3=y[49,1]-300
    ans=a2
    F1=F2
    F2=F3
    a1=a2
    a2=a3
    k=y[49,1]-300
    if k < 0:
        k= -1 * k
    err=k  
#print ans # TB0
#print y[9,0] #TA(n-1)
#Qa=1*(4000*(400-y[49,0])+5*(400**2-(y[49,0])**2)+10**(-2)/3*(400**3-(y[49,0])**3))
#Qb=-2*(3000*(300-ans)+2.5*(300**2-(ans)**2)+2*10**(-2)/3*(300**3-(ans)**3))
#print Qa
#print Qb
def qA(T):
    return 4000+10*T+10**(-2)*T**2
[Qa,err]=quad(qA,y[49,0],400)
#print Qa

def qB(T):
    return -2*(3000+5*T+2*10**(-2)*T**2)
[Qb,err]=quad(qB,ans,300)
#print Qb

percent_error4=(Qb-Qa)/Qa*100
print percent_error4

n=70
a1=307
t=linspace(0.0,9.0,70)
yinitial=([400,a1])
y=odeint(deriv,yinitial,t)
F1=y[69,1]-300
#print F1

a2=308
t=linspace(0.0,9.0,70)
yinitial=([400,a2])
y=odeint(deriv,yinitial,t)
F2=y[69,1]-300
#print F2
err=1
while (err>0.00000001):  
    a3=a2-(a2-a1)*F2/(F2-F1)
    t=linspace(0.0,9.0,70)
    yinitial=([400,a3])
    y=odeint(deriv,yinitial,t)
    F3=y[69,1]-300
    ans=a2
    F1=F2
    F2=F3
    a1=a2
    a2=a3
    k=y[69,1]-300
    if k < 0:
        k= -1 * k
    err=k  
#print ans # TB0
#print y[69,0] #TA(n-1)
#Qa=1*(4000*(400-y[69,0])+5*(400**2-(y[69,0])**2)+10**(-2)/3*(400**3-(y[69,0])**3))
#Qb=-2*(3000*(300-ans)+2.5*(300**2-(ans)**2)+2*10**(-2)/3*(300**3-(ans)**3))
#print Qa
#print Qb
def qA(T):
    return 4000+10*T+10**(-2)*T**2
[Qa,err]=quad(qA,y[69,0],400)
#print Qa

def qB(T):
    return -2*(3000+5*T+2*10**(-2)*T**2)
[Qb,err]=quad(qB,ans,300)
#print Qb

percent_error5=(Qb-Qa)/Qa*100
print percent_error5

n=100
a1=307
t=linspace(0.0,9.0,100)
yinitial=([400,a1])
y=odeint(deriv,yinitial,t)
F1=y[99,1]-300
#print F1

a2=308
t=linspace(0.0,9.0,100)
yinitial=([400,a2])
y=odeint(deriv,yinitial,t)
F2=y[99,1]-300
#print F2
err=1
while (err>0.00000001):  
    a3=a2-(a2-a1)*F2/(F2-F1)
    t=linspace(0.0,9.0,100)
    yinitial=([400,a3])
    y=odeint(deriv,yinitial,t)
    F3=y[99,1]-300
    ans=a2
    F1=F2
    F2=F3
    a1=a2
    a2=a3
    k=y[99,1]-300
    if k < 0:
        k= -1 * k
    err=k  
#print ans # TB0
#print y[9,0] #TA(n-1)
#Qa=1*(4000*(400-y[99,0])+5*(400**2-(y[99,0])**2)+10**(-2)/3*(400**3-(y[99,0])**3))
#Qb=-2*(3000*(300-ans)+2.5*(300**2-(ans)**2)+2*10**(-2)/3*(300**3-(ans)**3))
#print Qa
#print Qb
def qA(T):
    return 4000+10*T+10**(-2)*T**2
[Qa,err]=quad(qA,y[99,0],400)
#print Qa

def qB(T):
    return -2*(3000+5*T+2*10**(-2)*T**2)
[Qb,err]=quad(qB,ans,300)
#print Qb

percent_error6=(Qb-Qa)/Qa*100
print percent_error6

yerr=[percent_error1,percent_error2,percent_error3,percent_error4,percent_error5,percent_error6]
n=[10,20,30,50,70,100]
figure()
plot(n,yerr)
xlabel('n')
ylabel('% error')
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 10:21:59 2016

@author: user
"""
from scipy.integrate import odeint
from scipy import linspace
from scipy import array
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimization
                 # Data 
kla=0.07#m/s    Perry's Handbook Page 23 44
A=.5#m2
pT=1#"""atm"
Hc=29.4#"""atm/M""" ## Compilation of Henrys Law constants for inorganic and organic species of potential importance in Environmental Chemistry
MDc=4.089*10**(-2)#"M"
Hm=714.286#"atm/M" # Compilation of Henrys Law constants for inorganic and organic species of potential importance in Environmental Chemistry
MDm=4.1*10**(-2)#"M"
kGa=.00002#kmole.m/s.atm Perry's Handbook Page 23 44
Pwsat=0.03125#"atm"
H=1 #m
             # Defination of derivative function
def derivate(y,t):
    yc=y[0]/(y[0]+y[1]+y[2])#mole fraction of carbon dioxide in gaseous stream 
    ym=y[1]/(y[0]+y[1]+y[2])#mole fraction of methane in gaseous stream
    yw=y[2]/(y[0]+y[1]+y[2])#mole fraction of water in gaseous stream
    xc=y[3]/(y[3]+y[4]+y[5])#mole fraction of carbon dioxide in liquid stream
    xm=y[4]/(y[3]+y[4]+y[5])#mole fraction of methane in liquid stream
    #xw=y[5]/(y[3]+y[4]+y[5])
    dGc=-kla*A*(yc*pT/Hc-MDc*xc)
    dLc=-kla*A*(yc*pT/Hc-MDc*xc)
    dGm=-kla*A*(ym*pT/Hm-MDm*xm)
    dLm=-kla*A*(ym*pT/Hm-MDm*xm)
    dGw=kGa*A*(pT*yw-Pwsat)
    dLw=kGa*A*(pT*yw-Pwsat)
    return array([dGc,dLc,dGm,dLm,dGw,dLw])
#a=array ([5,5,80])
t=linspace(0.0,1.0,100)#range
              # Defination of Error function
def error(x,a,b,c):
    #t=linspace(0.0,10.0,100)
    yinitial=([50,a,50,b,0,c])
    y=odeint(derivate,yinitial,t)
    return array([y[99,5],y[99,3],y[99,1]])

xdata=array([10])
ydat=array([100,0,0])
ydata=np.transpose(ydat)
print ydata
x0=array([10,5,90])
                 # Actual Optimization step
([ans,err])=optimization.curve_fit(error,xdata,ydata,x0)
print ans
yinitial=([50,ans[0],50,ans[1],0,ans[2]])
y=odeint(derivate,yinitial,t)
print y[99,:]
print yinitial
                   #  Plotting 
# Gw Vs Height    
fig=plt.figure()
ax=fig.add_subplot(111)
plt.plot(t,y[:,4],'r')#Gw
ax.title.set_text('Gw Vs height')
ax.xaxis.label.set_text('height')
ax.yaxis.label.set_text('Gw')
plt.show()
# Gc Vs Height
fig=plt.figure()
ax=fig.add_subplot(111)
plt.plot(t,y[:,0],'g')#Gc
ax.title.set_text('Gc Vs height')
ax.xaxis.label.set_text('height')
ax.yaxis.label.set_text('Gc')
plt.show()
# Gm Vs Height
fig=plt.figure()
ax=fig.add_subplot(111)
plt.plot(t,y[:,2],'b')#Gm
ax.title.set_text('Gm Vs height')
ax.xaxis.label.set_text('height')
ax.yaxis.label.set_text('Gm')
plt.show()
fig=plt.figure()
ax=fig.add_subplot(111)
plt.plot(t,y[:,1],'r')#Lc
ax.title.set_text('Lc Vs height')
ax.xaxis.label.set_text('height')
ax.yaxis.label.set_text('Lc')
plt.show()

fig=plt.figure()
ax=fig.add_subplot(111)
plt.plot(t,y[:,3],'r')#Lm
ax.title.set_text('Lm Vs height')
ax.xaxis.label.set_text('height')
ax.yaxis.label.set_text('Lm')
plt.show()

fig=plt.figure()
ax=fig.add_subplot(111)
plt.plot(t,y[:,5],'r')#Lw
ax.title.set_text('Lw Vs height')
ax.xaxis.label.set_text('height')
ax.yaxis.label.set_text('Lw')
plt.show()
           # Percentage Error
per_error=(200-(y[99,0]+y[99,1]+y[99,2]+y[99,3]+y[99,4]+y[99,5]))/2
print per_error
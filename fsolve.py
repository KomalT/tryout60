# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 19:54:54 2016

@author: user
"""
from scipy.integrate import odeint
from scipy import linspace
from scipy import array
import numpy
from scipy.optimize import fsolve
def deri(y,t):
    return t
a=2
t=linspace(0.0,1.0,10)
def err(a):
    t=linspace(0.0,1.0,10)
    yinitial=a
    y=odeint(deri,yinitial,t)
    return y[9]-1.5
ans=fsolve(err,a)
print ans
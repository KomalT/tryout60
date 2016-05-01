# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 20:39:58 2016

@author: u
"""
import math
import matplotlib.pyplot as plt
import numpy
d = 0.1 # plate thickness
Pdrop = -100
mu = 1

def odefun(U, y):
    u1, u2 = U
    du1dy = u2
    du2dy = 1.0 / mu * Pdrop
    return [du1dy, du2dy]

x1 = 0.0; alpha = 0.0
x2 = 0.1; beta = 0.0
init = 2.0 # initial guess of slope at x=0

y = shoot(odefun, x1, x2, alpha, beta, init)
print X
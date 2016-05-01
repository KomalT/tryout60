# -*- coding: utf-8 -*-
"""
Created on Sat Jan 09 22:01:51 2016

@author: user
"""
from scipy import array
import numpy as np
x1= array([1,2])
x2= array([1,2])
x3=np.multiply(x1,x2)
print x3
x4=x3-np.divide((x2-x1),x3)
print x4
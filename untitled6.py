# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 21:32:14 2016

@author: JUILI
"""



import math
import numpy as np
L=1 # m (CE lab experiment Hyroynamics of bubble column)
D=.0778 # m (CE lab experiment Hyroynamics of bubble column)
Ar=3.14*D**2/4
V=3.14*D**2*L/4
kla=.0002 #1/s Mass transfer Coefficient
kga=.00002 #gmol/m^2-Pa-s Mass transfer Coefficient
P=1 # (atm)
T=80 #'C
# (Antoine constant for water -Ce lab Manual Sem5)
A=18.3036 
B=3816.44
C=-46.13
Psat=math.exp(A-(B/(T+C+273.16)))
de=([0.52294373, 0.55410293173585])# kg/ m^3 http://www.peacesoftware.de/einigewerte/calc_co2.php5,http://www.peacesoftware.de/einigewerte/calc_methan.php5
d=np.zeros(2)
d[1]=de[1]*1000/16 # gmole/m^3
d[0]=de[0]*1000/44
#print Psat
# Henry's coeffiecient
hin=np.array([.034,.0014])# (in M/atm at T=298.15K)
div=np.array([2400,1700]) #(Factor accounting for operating temperature condition)
R=8.314 # J/K mole
#h=np.zeros(1)
z=np.zeros(2)
#print z
delH=np.zeros(2)
h=np.zeros(2)
delH=-div*R
#print delH
z=np.exp(-delH*(298.15-(T+273.16))/(R*(T+273.16)*298.15))
#print z
h=hin*z # Henry coefficient [CO2,CH4] 
# Gas inlet Stream
yM=.5
yC=.5
yW=0
Gc1=50
Gm1=50
Gw1=0
# Liquid outlet initial guess
xM=.3
xC=.3
xW=.4
Lm1=30
Lc1=30
Lw1=40
P1=101325
dz=1/50
e1=10
e2=10
e3=10
while e1>.1 or e2>.1 or e3>.1:
    Gc2=Gc1-dz*(kla*A*((h[0]*P*yC*1000)-d[0]*xC))*3600
    Gm2=Gm1-dz*(kla*A*((h[1]*P*yM*1000)-d[1]*xM))*3600  
    Lc2=Lc1-dz*(kla*A*((h[0]*P*yC*1000)-d[0]*xC))*3600
    Lm2=Lm1-dz*(kla*A*((h[1]*P*yM*1000)-d[1]*xM))*3600 
    Gw2=Gw1+dz*(kga*A*(P1*yW-(Psat*101325/760)))*3600
    Lw2=Lw1+dz*(kga*A*(P1*yW-(Psat*101325/760)))*3600
    yC=Gc2/(Gc2+Gm2+Gw2)
    yM=Gm2/(Gc2+Gm2+Gw2)
    yW=1-yC-yM
    yC=Lc2/(Lc2+Lm2+Lw2)
    yM=Lm2/(Lc2+Lm2+Lw2)
    yW=1-yC-yM
    e1=yC
    e2=yM
    e3=abs(yW-1)
    Gc1=Gc2
    Gm1=Gm2
    Gw1=Gw2
    Lc1=Lc2
    Lm1=Lm2
    Lw1=Lw2
    print Gm1

    
    
    
    
    
    
    
    
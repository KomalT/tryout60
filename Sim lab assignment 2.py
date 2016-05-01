# -*- coding: utf-8 -*-
"""
Created on Sat Jan 09 22:54:12 2016

@author: MIT
"""
import scipy
Pt=760#mmhg
T=500
A=2*10**(-3)#cross sectional area of the contactor 
Vg=100#
Vl=100
n=int(input("n= "))
h=10.0#height of the contactor 
dz=h/(n-1)
kla1=0.0005;kla2=0.0005;kla3=0.0005
H2=714.5;H1=714.5;
Pws=scipy.exp(18.3036-3816.44/T-46.13)
Gw=0;Gco2=0.5*Vg;Gch4=0.5*Vg
Lw=Vl;Lc=0;Lm=0
d1=0.041;d2=0.041;d3=0.041
R=8.314;
m=0
e=0.2;e1=0.2;e2=0.2;e3=0.2;
while e>0.00001:
    Gw=0;Gc=0.5*Vg;Gm=0.5*Vg
    if e2>0.001:
        Lc=(0+m*0.001)*Vl
    if e3>0.001:
        Lm=(0+m*0.001)*Vl
    if e1>0.001:
        Lw=1*Vl-Lc-Lm;
    for i in range(n):
        dg1dz=-kla1*A*((Gc*Pt/((H1*(Gw+Gc+Gm)))-(d1*Lc)/(Lw+Lc+Lm)));
        Gc=Gc+dg1dz*dz;
        dg2dz=-kla2*A*((Gm*Pt/((H2*(Gw+Gc+Gm)))-(d2*Lm)/(Lw+Lc+Lm)));
        Gm=Gm+dg2dz*dz;
        dg3dz=-kla3*A*((Gw*Pt/((R*T*(Gw+Gc+Gm))))-Pws/R*T);
        Gw=Gw+dg3dz*dz;
        #dl1dz=-kla1*area*((Gco2*Pt/((H1*(Gw+Gco2+Gch4))))-(d1*Lco2)/(Lw+Lco2+Lch4));
        dl1dz=dg1dz
        Lc=Lc-dl1dz*dz;
    
        #dl2dz=-kla2*area*((Gch4*Pt/((H2*(Gw+Gco2+Gch4))))-(d2*Lco2)/(Lw+Lco2+Lch4));
        dl2dz=dg2dz
        Lm=Lm-dl2dz*dz;
        Lw=(Vl+Vg)-(Lc+Lm+Gc+Gw+Gm);
    e1=100-Lw;
    #e2=Lco2/Vl;
    #e3=Lch4/Vl;
    e2=Lc;
    e3=Lm;
    e=e1*e2*e3;
    print e1,e2,e3
    m=m+1;
print Lw;
print Lc;
print Lm;
print Gw;
print Gm;
print Gc;    
    

    
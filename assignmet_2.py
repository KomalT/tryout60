# -*- coding: utf-8 -*-
"""
Created on Sat Jan 09 21:21:24 2016

@author: Hp
"""

import scipy
from scipy.integrate import odeint
from scipy import linspace
#CONTINUOUS CONTACTING EQUIPMENT
#COMPONENTS: 1. CO2 2.CH4 3.H2O
pt=101325 # (atm) #total pressure of the system
T= 300 #  (Kelvin) Temperature of the system
d=0.075 # (cm) diameter of column 
area=0.25*scipy.pi*d*d #Area of cross section
Vgas=100.0 #(kmol/s)
Vliq=100.0 #(kmol/s)
n=10; #no of points
h=10.0 #(m) height of column
dz=h/(n-1);
kla1=0.07; kla2=0.07; kgaw=0.002; #overall mass transfer coefficients
H1=2.97619; H2=72.325; #Henry's constants for CO2 and CH4 repectively
pwsat=133.3224*scipy.exp(18.3036-3816.44/(T-46.13)) #(Pa)
Gw=0; Gco2=0.5*Vgas; Gch4=0.5*Vgas;
Lw=1*Vliq; Lco2=0; Lch4=0;
e=1;e1=1;e2=1;e3=1;
ro1=0.04494; ro2=0.04474;ro3=55.55; #densities of CO2, CH4 and H2O respectively
R=8.314 #
m=0;
#####Conversions into SI Units#########
while e>0.0000001:
    Gw=0; Gco2=0.5*Vgas; Gch4=0.5*Vgas;
    if e2>0.001:
        Lco2=(0+m*0.01)*Vliq; 
    if e3>0.001:
        Lch4=(0+m*0.001)*Vliq;
    if e1>1:
        Lw=1*Vliq-Lco2-Lch4;
    for i in range(n):
        
        def epid(Gco2,h):
           dg1dz=(-kla1*area*((Gco2*pt/((H1*(Gw+Gco2+Gch4))))-(ro1*Lco2)/(Lw+Lco2+Lch4)))
           return dg1dz
           
           
        h=linspace(0,9,n)
        Gco2=odeint(epid,Gco2,h)      
        epid_solve=odeint(epid,Gco2,h)
        print Gco2[9]
        def epid2(Gch4,h):
           dg2dz= -kla2*area*((Gch4*pt/((H2*(Gw+Gco2+Gch4))))-(ro2*Lch4)/(Lw+Lco2+Lch4))
           return dg2dz
        
    h=linspace(0,9,n)
    Gch4=odeint(epid2,Gw,Gco2,Gch4,Lw,Lco2,Lch4,h) 
    epid_solve=odeint(epid2,Gch4,h)   
       
    def epid3(Gw,h):
           dg3dz= -kgaw*area*(Gw*pt/((R*T*(Gw+Gco2+Gch4)))-pwsat/(R*T))
           return dg3dz
        
        
    h=linspace(0,9,n)
    Gw=odeint(epid3,Gw,Gco2,Gch4,Lw,Lco2,Lch4,h)  
    epid_solve=odeint(epid3,Gw,h)
     
     
    def epid4(Lco2,h):
           dl1dz=-kla1*area*((Gco2*pt/((H1*(Gw+Gco2+Gch4))))-(ro1*Lco2)/(Lw+Lco2+Lch4))
           return dl1dz
        
        
    h=linspace(0,9,n)
    Lco2=odeint(epid4,Gw,Gco2,Gch4,Lw,Lco2,Lch4,h)  
    epid_solve=odeint(epid4,Lco2,h)

    def epid5(Lch4,h):
           dl2dz=-kla2*area*((Gch4*pt/((H2*(Gw+Gco2+Gch4))))-(ro2*Lch4)/(Lw+Lco2+Lch4))
           return dl2dz
        
        
    h=linspace(0,9,n)
    Lch4=odeint(epid5,Gw,Gco2,Gch4,Lw,Lco2,Lch4,h)  
    epid_solve=odeint(epid5,Lch4,h)
          
    Lw=(Vliq+Vgas)-(Lco2+Lch4+Gco2+Gch4+Gw);
    e1=100-Lw;
    e2=Lco2/Vliq;
    e3=Lch4/Vliq;
    e=e1*e2*e3;
    print e1,e2,e3
    m=m+1;
print Gco2;
print Gch4;
print Gw;
print Lco2;
print Lch4;
print Lw;
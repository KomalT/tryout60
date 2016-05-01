# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 10:55:45 2016

@author: KT
"""
import math
import linspace
n=60
#**** TUBE SIDE(OIL)  *********
Cph=3000           #   *J/Kg K
Roh=850            #   *Kg/m3
Meuh=0.001+n/50    #   *Pa s
Kh=.45             #   *W/m2K 
Thin=120           #   *Deg
Thout=70           #   *Deg
Qh1=500+10*n       #   *LPM
Qh=Qh1*10**(-3)/60 #   *m3/sec
mh=Qh*Roh          #   *Kg/sec

#**** SHELL SIDE(WATER)  *********
Cpc=4000           #   *J/Kg K
Roc=1000           #   *Kg/m3
Meuc=0.001         #   *Pa s
Kc=.6              #   *W/m2K 
Tcin=32            #   *Deg
Tcout=37           #   *Deg
mc=mh*Cph*(Thin-Thout)/(Cpc*(Tcout-Tcin))

Qoverall=mh*Cph*(Thin-Thout)

#  ***  Assumptions ****
#  COUNTER CURRENT  AND SQUARE LAYOUT
DeltaTlm=((Thin-Tcout)-(Thout-Tcin))/(math.log((Thin-Tcout)/(Thout-Tcin)))
print DeltaTlm

#  *** U RANGE *****
Ur=linspace(110,340,10)
#  ****  AVAILABLE PARAMETERS ***
# *****  TUBE DIMENSIONS ****
di=.02  # Inner dia of tube * m *
L=2     # Length of tube    *m*   
t=0.002   # Thickness 
do=.022  # outer dia

# **** CALCULATION OF TUBE SIDE VELOCITY ***
def velocity(F,npass):
    A=Qoverall/(U*DeltaTlm*F)
    Ntubes=round(A/(22/7*do*L))
    Nfill=Ntubes/npass
    Across=22/(7*4)*round(Nfill)*di**(2)
    v=Qh/Across
    return array([v,Ntubes,round(Nfill)]

# *** CALCULATIONS OF SHELL SIDE DIMENSIONS ***
def shell():
    













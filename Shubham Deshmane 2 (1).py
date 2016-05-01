# -*- coding: utf-8 -*-
"""
Created on Sat Jan 09 14:30:27 2016

@author: Shubham Deshmane
"""

import scipy
import matplotlib.pyplot as plt
import scipy.optimize as opti
#DATA from various sources
Kla=[0.004,0.004]#1/s for carbon dioxide and methane
Kga=0.0002#1/s for water
A=10.0#m^2 packed column area
H=[29.4,714.286]#atm/mol for compds CH4 and CO2
TP=10;Pwsat=0.041#atm total presuure of system and sat.pressure for T=300K
MD=[55.55,0.04088,0.041]#mol/m^3 molar densities for each compound H2O,CO2,CH4
n=10;L=10.0#m length of packed column
Gwin=0.0;Gcin=50.0;Gmin=50.0;#Molar both are the flow rates in mol/hr
Lwin=100.0;Lcin=0.0;Lmin=0.0;#molar
Gwguess=n*[Gwin];Gcguess=n*[Gcin];Gmguess=n*[Gmin]#guesses for all reqired composition
Lwguess=n*[Lwin];Lcguess=n*[Lcin];Lmguess=n*[Lmin]
#print Gwguess
totalguess=scipy.array(Gwguess+Gcguess+Gmguess+Lwguess+Lcguess+Lmguess)
#now using residuals method we can minimize the error
#for tht Yi and Xi is the function of gas and liquid flow rates at tht point
#so define function for mole fractions Yi,Xi

def yw(Gw,Gc,Gm):
    yw=(Gw)/((Gw+Gc+Gm))
    return yw
def yc(Gw,Gc,Gm):
    yc=(Gc)/((Gw+Gc+Gm))
    return yc    
def ym(Gw,Gc,Gm):
    ym=(Gm)/((Gw+Gc+Gm))
    return ym
def xw(Lw,Lc,Lm):
    xw=(Lw)/((Lw+Lc+Lm))
    return xw    
def xc(Lw,Lc,Lm):
    xc=(Lc)/((Lw+Lc+Lm))
    return xc
def xm(Lw,Lc,Lm):
    xm=(Lm)/((Lw+Lc+Lm))
    return xm
#define residuals and using known quantites cal errors    
#S includes total flow rates ,its array of [Gw,Gc,Gm,Lw,Lc,Lm]    
   # and then SW is for gas flow rates and SW1 is for liqid flow rates 
def residuals(S,L,A,H,Kla,MD,TP,Kga):
    n=len(S)
    SW=S[:n/6];SC=S[n/6:n/3];SM=S[n/3:n/2]#G
    SW1=S[n/2:2*n/3];SC1=S[2*n/3:5*n/6];SM1=S[5*n/6:]#l
    dx=L/(n-1)
    #forward difference
    errorGWBHS=((SW[1]-Gwin)/dx)+Kga*A*(TP*yw(Gwin,Gcin,Gmin)-Pwsat)
    errorGCBHS=((SC[1]-Gcin)/dx)+Kla[0]*A*(((TP*yc(Gwin,Gcin,Gmin))/H[0])-xc(Lwin,Lwin,Lmin)*MD[1])
    errorGMBHS=((SM[1]-Gmin)/dx)+Kla[1]*A*(((TP*ym(Gwin,Gcin,Gmin))/H[1])-xm(Lwin,Lwin,Lmin)*MD[2])
    
    errorLWBHS=((SW1[1]-Lwin)/dx)+Kga*A*(TP*yw(Lwin,Lcin,Lmin)-Pwsat)
    errorLCBHS=((SC1[1]-Lcin)/dx)+Kla[0]*A*(((TP*yc(Gwin,Gcin,Gmin))/H[0])-xc(Lwin,Lwin,Lmin)*MD[1])
    errorLMBHS=((SM1[1]-Lmin)/dx)+Kla[1]*A*(((TP*ym(Gwin,Gcin,Gmin))/H[1])-xm(Lwin,Lwin,Lmin)*MD[2])
    #backward diffrence
    errorGWTHS=((SW[-1]-SW[-2])/dx)+Kga*A*(TP*yw(SW[-1],SC[-1],SM[-1])-Pwsat)
    errorGCTHS=((SC[-1]-SW[-2])/dx)+Kla[0]*A*(((TP*yc(SW[-1],SC[-1],SM[-1]))/H[0])-xc(SW1[-1],SC1[-1],SM1[-1])*MD[1])
    errorGMTHS=((SM[-1]-SW[-2])/dx)+Kla[1]*A*(((TP*ym(SW[-1],SC[-1],SM[-1]))/H[1])-xm(SW1[-1],SC1[-1],SM1[-1])*MD[2])
    
    errorLWTHS=((SW1[-1]-SW1[-2])/dx)+Kga*A*(TP*yw(SW[-1],SC[-1],SM[-1])-Pwsat)
    errorLCTHS=((SC1[-1]-SC1[-2])/dx)+Kla[0]*A*(((TP*yc(SW[-1],SC[-1],SM[-1])/H[0])-xc(SW1[-1],SC1[-1],SM1[-1])*MD[1]))
    errorLMTHS=((SM1[-1]-SM1[-2])/dx)+Kla[1]*A*(((TP*ym(SW[-1],SC[-1],SM[-1])/H[1])-xm(SW1[-1],SC1[-1],SM1[-1])*MD[2]))
    #for central difference
    errorBW=scipy.zeros(n/6)
    errorBC=scipy.zeros(n/6)
    errorBM=scipy.zeros(n/6)
    errorTW=scipy.zeros(n/6)
    errorTC=scipy.zeros(n/6)
    errorTM=scipy.zeros(n/6)
    errorBW[0]=errorGWBHS;errorBW[-1]=errorGWTHS
    errorBC[0]=errorGCBHS;errorBC[-1]=errorGCTHS
    errorBM[0]=errorGMBHS;errorBM[-1]=errorGMTHS
    errorTW[0]=errorLWBHS;errorTW[-1]=errorLWTHS
    errorTC[0]=errorLCBHS;errorTC[-1]=errorLCTHS
    errorTM[0]=errorLMBHS;errorTM[-1]=errorLMTHS
    #central Difference
    errorBW[1:-1]=((SW[2:]-SW[1:-1])/dx)+Kga*A*(TP*yw(SW[1:-1],SC[1:-1],SM[1:-1])-Pwsat)
    errorBC[1:-1]=((SC[2:]-SC[1:-1])/dx)+Kla[0]*A*(((TP*yc(SW[1:-1],SC[1:-1],SM[1:-1]))/H[0])-xc(SW1[1:-1],SC1[1:-1],SM1[1:-1])*MD[1])
    errorBM[1:-1]=((SM[2:]-SC[1:-1])/dx)+Kla[1]*A*(((TP*yc(SW[1:-1],SC[1:-1],SM[1:-1]))/H[1])-xm(SW1[1:-1],SC1[1:-1],SM1[1:-1])*MD[2])
    errorTW[1:-1]=((SW1[2:]-SW1[1:-1])/dx)+Kga*A*(TP*yw(SW[1:-1],SC[1:-1],SM[1:-1])-Pwsat)
    errorTC[1:-1]=((SC1[2:]-SC1[1:-1])/dx)+Kla[0]*A*(((TP*yc(SW[1:-1],SC[1:-1],SM[1:-1]))/H[0])-xc(SW1[1:-1],SC1[1:-1],SM1[1:-1])*MD[1])
    errorTM[1:-1]=((SM1[2:]-SC1[1:-1])/dx)+Kla[1]*A*(((TP*yc(SW[1:-1],SC[1:-1],SM[1:-1]))/H[1])-xm(SW1[1:-1],SC1[1:-1],SM1[1:-1])*MD[2])
    return scipy.concatenate((errorBW,errorBC,errorBM,errorTW,errorTC,errorTM))
#syntax for optimization
n=len(totalguess) 
ans=opti.leastsq(residuals,totalguess,args=(L,A,H,Kla,MD,TP,Kga))
#required answer  is zeroth element of ans array
print (ans)
Tans=ans[0]
print Tans
GWans=Tans[:n/6]
GCans=Tans[n/6:n/3]
GMans=Tans[n/3:n/2]
LWans=Tans[n/2:2*n/3]
LCans=Tans[2*n/3:5*n/6]
LMans=Tans[5*n/6:]
print(GWans)
print(GCans)
print(GMans)
print(LWans)
#print(LCans)
#print(LMans)
b=scipy.linspace(0,100,10)
plt.plot(b,GWans,'r')
plt.show()
plt.plot(b,GCans,'b')
plt.show()
plt.plot(b,GMans,'g')
plt.show()
#plt.plot(b,LWans,'g')
#plt.show()
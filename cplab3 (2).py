import matplotlib.pyplot as plt
from scipy import array
import scipy.optimize
Mdm=0.04175 #molar density gmol/Lit of methane ref 3
Hm=714.2857 #henry's coef of methane atm*lit/gmol ref2
Mdc=0.04186 #molar density gmol/Lit of co2 ref 3
Hc=29.76 #henry's coef of CO2 atm*lit/gmol ref 3
pwsat=0.03125 #atm ref3
pT=1 #atm
kla=0.008 #sec-1 ref1
Lc=0#initial guess for co2 in liq
Lm=0#initial guess for methane in liq
Lw=100#initial guess for water in liq
Gc=50#known co2 flow rate
Gm=50#known methane flow rate
Gw=0#known initial water in gas
L=10#meter
R=0.0821#atm/molK
T=298#K

Lt=[Lc,Lm,Lw]
Gt=[Gc,Gm,Gw]
#p=range(10)
#for j in range(6):
err1,err2,err3=1,1,1
kga=7*10^-7
error=1;Lc=0#initial guess for co2 in liq;
Lm=0#initial guess for methane in liq
Lw=100#initial guess for water in liq
Gc=50#known co2 flow rate
Gm=50#known methane flow rate
Gw=0#known initial water in gas
Lt=[Lc,Lm,Lw]
Gt=[Gc,Gm,Gw]
Lexp=[0,0,100]
def absorption(Gc,Gm,Gw,Lc,Lm,Lw):
    for i in range (10):
        h=L/(10-1)
        yc=Gc/(Gc+Gm+Gw)
        ym=Gm/(Gc+Gm+Gw)
        yw=Gw/(Gc+Gm+Gw)
        xc=Lc/(Lc+Lm+Lw)
        xm=Lm/(Lc+Lm+Lw)
        #xw=Lw/(Lc+Lm+Lw)
        Gc1=Gc-h*kla*(pT*yc/Hc-xc*Mdc)
        Gm1=Gm-h*kla*(pT*ym/Hm-xm*Mdm)
        Gw1=Gw+h*kga*(pT*yw-pwsat)
        Lc1=Lc-h*kla*(pT*yc/Hc-xc*Mdc)
        Lm1=Lm-h*kla*(pT*ym/Hm-xm*Mdm)
        Lw1=Lw+h*kga*(pT*yw-pwsat)
        Gc=Gc1
        #print Gc
        Gm=Gm1
        Gw=Gw1
        Lc=Lc1
        Lm=Lm1
        Lw=Lw1
    a=Lc;b=Lm;c=Lw;
    return array([a,b,c])
def error(x,a,b,c):
    
    a11=absorption(50,50,0,a,b,c)
    err1=a11[0]-Lexp[0]
    err2=a11[1]-Lexp[1]
    err3=a11[2]-Lexp[2]
    err=[err1,err2,err3]
    return err
Lguess=[10,10,80]
xdata=array([10])
ydata=array([0,0,0])
Lans=scipy.optimize.curve_fit(error,xdata,ydata,Lguess)
La=Lans[0] 
print La    

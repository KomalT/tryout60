# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 20:53:53 2016

@author: Komal
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import scipy as sc
import win32com.client as win32
from scipy import array
import numpy as np
import scipy,scipy.optimize
import matplotlib.pyplot as plt
from math import log
from math import exp
from math import sqrt
import scipy.optimize as optimization
from scipy.optimize import curve_fit
import pandas as pd
import numdifftools as nd
w=[0.05,0.10,0.202,0.297,0.402,0.501]
P=[12.13,11.78,11.28,10.65,9.94,8.73]
T=323.15
Mwt=84.9947
N=[0.11670521452767*(10**4),-724213.16703206,-17.073846940092,0.12020824702470*(10**5),-3232555.0322333,0.14915108613530*(10**2),-4823.2657361591,0.40511340542057*(10**6),-0.23855557567849,0.65017534844798*(10**3)]
R=8.314
v=T+(N[8]/(T-N[9]))
#print v
A=v**2+N[0]*v+N[1]
#print A
B=N[2]*v**2+N[3]*v+N[4]
C=N[5]*v**2+N[6]*v+N[7]
VP=(2*C/(-B+(B**2-4*A*C)**0.5))**4 ##MPa
#print VP
#VP=0.0123513 #MPa
##DATA

N1=w/MWt;
N2=(1-w)/18;
Ntotal=N1+N2;
x=np.divide(N2,Ntotal)
x1=np.divide((1-x),(2-x));   ##xNa+
x2=np.divide((1-x),(2-x));   ##xNO3-
x3=np.divide((x),(2-x));     ##xH2O

P=np.transpose(P)
#print x1
#print x2
#print x3
#plot(x3,P,'+')
##DEBYE-HUCKEL PART
##1.gama calc
s=-61.4453*exp((T-273.15)/273.15)+2.864468*((exp((T-273.15)/273.15))**2)+183.379*log(T/273.15)-.6820223*(T-273.15)+.0007875695*(T**2-273.15**2)+58.95788*273.15/T;
I=([(x1+x2)/2]);
#print I
k111=sqrt(1000/18)*s*(2*np.divide(np.power(I,1.5),(1+14.9*np.power(I,.5))))

#V=([exp(sqrt(1000/18)*s*(2*np.divide(np.power(I,1.5),(1+14.9*np.power(I,.5)))))]);
V1=np.exp(k111)
V=V1
#print V
#NRTL PART
#T(m,ca)=A(1) T(ca,m)=A(2) alpha(ca,m)=A(3) G(ca,m)=K G(m,ca)=L
#Z=[P;x1;x2;x3;V];
#Z=np.concatenate((P,x1,x2,x3,V))
A0=[2,0,2,0,0,2]
#x=np.concatenate((x1,x2,x3))
x=np.array([x1,x2,x3,V])
#print x
x=np.transpose(x)
Z=np.array([x1,x2,x3,V,P])
#x1=x(0)
#print x1
def datafit_1(x,A):
    x1=x[0]
    x2=x[1]
    x3=x[2]
    V=x[3]
    #a,b,c=A
    T2=A[1]+A[3]/T+A[5]*log(T)   #A(2)+A(4)/T+A(5)*log(T);
    T1=A[0]+A[2]/T+A[4]*log(T)   #A(1)+A(3)/T+A(6)*log(T);
    K=exp(-0.2*T2);
    L=exp(-0.2*(T1));
    B1=(2*K*(T2)*x1)/(K*(2*x1)+x3);
    B2=(2*K*(T2)*x1*x3)/((K*(2*x1)+x3)**2);
    B3=(L*x1/(x2+L*x3))*((T1)-(L*(T1)*x3)/(x2+L*x3));
    B4=(L*x2/(x1+L*x3))*((T1)-(L*(T1)*x3)/(x1+L*x3));
    U=np.exp(B1-B2+B3+B4);
    y=1000*VP*x3*U*V;
    return y





def myerror(A,z):
    #x1=z(1);x2=z(2);x3=z(3);V=z(4);P=z(5);
    x1,x2,x3,V,P=z
    #a,b=A
    x=np.array([x1,x2,x3,V])
    e= P - datafit_1(x,A)
    return e[0]



ans1=scipy.optimize.leastsq(myerror,A0,Z)
ans=ans1[0]
print ans
a,b,c,d,e,f=ans
ycalc=datafit_1(x,ans)
fig=plt.figure();
ax=fig.add_subplot(111)
#ax.plot(x[2],P,'*')
#ax.plot(x[2],ycalc[0],'b')    
#ax.title.set_text('P Vs x3')
fig.canvas.draw()
plt.show()
T2=b+d/T+f*log(T)   #A(2)+A(4)/T+A(5)*log(T);
T1=a+c/T+e*log(T)   #A(1)+A(3)/T+A(6)*log(T);


########    Gexcess calc  ############

g1=T2*R*T;
g2=T1*R*T;
x1=numpy.arange(0,0.5,0.01)
#x1=0:.01:.5;
x2=x1;
x3=(1-2*x1);
H1=[]
He1=[]
def data_fit_1(T1):
    s=-61.4453*exp((T1-273.15)/273.15)+2.864468*((exp((T1-273.15)/273.15))**2)+183.5379*log(T1/273.15)-.6820223*(T1-273.15)+.0007875695*(T1**2-273.15**2)+58.95788*273.15/T1;
    I=(t1+t2)/2;
    GeDH=R*(-sqrt(1000/18)*(s/14.9)*4*I*log((1+14.9*I**.5)/(1+14.9*.5**.5)));
    K=exp(-.2*g2/(R*T1));
    L=exp(-.2*g1/(R*T1));
    GeSR=(g1/(R*T1))*K*t3*(t1+t2)/(t3+K*(t1+t2))+(g2/(R*T1))*L*t3*((t1/(t2+L*t3))+(t2/(t1+L*t3)));
    G=GeDH+R*GeSR;
    return G
#funcprot(0)
    ##########  From the above function we can easily estimate Gexcess values 
    
    
    #@$$$$$$$$$$    Hexcess Calculations  
for i in range (1, 0.5/0.01):
    t1=x1[0,i];
    t2=x2[0,i];
    t3=x3[0,i];

    T1=333.15 ##//K
    #H1.append(data_fit_1.diff(T1))
    H1.append(nd.Derivative(data_fit_1,T1))
    He1.append(-H1(1,i)*T1**2);

ax.plot(x1,He1,'g')
fig.canvas.draw()
plt.show()

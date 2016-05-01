import scipy,scipy.optimize
import matplotlib.pyplot as plt
import numpy as np
from scipy import array
x=array([1164.42,1663.97,1950.45,3526.04,4319.63])
y=array([.03188,.03122,.025,.0125,.01158])
print y
def curve(x,p):
    [A,B]=p
    y=A*x**B
    return y
def error(p,x,y):
    err=y-curve(x,p)
    return err
def get_r2(x,y,ycalc):
    ymean=scipy.average(y)
    dymean2=(y-ymean)**2
    dycalc2=(y-ycalc)**2
    r2=1-sum(dycalc2)/sum(dymean2)
    return r2
pguess=[16,-1]
plsq=scipy.optimize.leastsq(error,pguess,args=(x,y))
p=plsq[0]
ycalc=curve(x,p)
r2=get_r2(x,y,ycalc)
print p
fig=plt.figure();
ax=fig.add_subplot(111)
ax.plot(x,y,'*')
ax.plot(x,ycalc,'b')    
ax.title.set_text('r2=%f'%(r2))
fig.canvas.draw()
plt.show()
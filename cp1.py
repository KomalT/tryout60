from scipy.integrate import odeint
from scipy import linspace
from scipy import array
import numpy
from scipy.integrate import quad
def deriv(y,t):
    U=100
    P=1
   
    
    return array([-U*P/(1*(4000+10*y[0]+10**(-2)*y[0]**2))*(y[0]-y[1]) , -U*P/(2*(3000+5*y[1]+2*10**(-2)*y[1]**2))*(y[0]-y[1])])
alpha=400
gamma0=320
beta=300
tol=0.00000001
t=linspace(0.0,9.0,10)
yinitial=([alpha,gamma0])
y=odeint(deriv,yinitial,t)
end1=y[9,1]-beta
print end1
gamma1=310
t=linspace(0.0,9.0,10)
yinitial=([alpha,gamma1])
y=odeint(deriv,yinitial,t)
end2=y[9,1]-beta
print end2
for i in range(10):  
    gamma=gamma1-(gamma1-gamma0)*(end2)/(end2-end1)
    t=linspace(0.0,9,10)
    yinitial=([alpha,gamma])
    y=odeint(deriv,yinitial,t)
    end3=y[9,1]
    end1=end2
    end2=end3
    gamma0=gamma1
    gamma1=gamma
    ans=gamma1
    error=end2-beta
    if error < tol:
        break
print ans
t1=ans
print y[9,0]
t2=y[9,0]
Qa=1*(4000*(400-t2)+5*(400**2-t2**2)+0.333*10**(-2)*(400**3-t2**3))
Qb=2*(3000*(t1-300)+2.5*(t1**2-300**2)+0.333*2*10**(-2)*(t1**3-300**3))
print Qa
print Qb
relerr=(Qa-Qb)*100/Qa
print relerr
def qA(T):
    return 4000+10*T+10**(-2)*T**2
[Qa,err]=quad(qA,y[9,0],400)
print Qa

def qB(T):
    return 2*(3000+5*T+2*10**(-2)*T**2)
[Qb,err]=quad(qB,ans,300)
print Qb

#from scipy.integrate import simps
#def qA(T):
    #return 4000+10*T+10**(-2)*T**2
#T=array([y[9,0],400])
#y=qA(T)
#Qa= integrate.simps(y,T)
#print Qa
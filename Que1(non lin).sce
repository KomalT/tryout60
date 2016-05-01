//REDLICK KWONG
clc;clear
R=8.314
Tc=416.3//K
Pc=66.8*10^(5)//pa
T=(273.16+60)//K
P=13.76*10^(5)//pa
a=.4275*R^2*Tc^2.5/Pc
b=.08664*R*Tc/Pc
V=(R*T)/P//initial guess
function f=F(V)
    f=P-R*T/(V-b)+a/(T^.5*V*(V+b));
endfunction
y = fsolve(V,F);
disp(y)//m3

//RECYCLE
//clc;clear
Xaf=.95
R=10
function f1=F1(R)
    f1=log((1+R(1-Xaf))/(R*(1-Xaf)))-(R+1)/(R*(1+R(1-Xaf)));
endfunction
//y1 = fsolve(R,F1);
//disp(y1)//m3

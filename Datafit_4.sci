clc;
clear;
r=[1.04 3.13 5.21 3.82 4.19 2.391 3.867 2.199 0.75]//Reaction Rate
et=[1 1 1 3 5 0.5 0.5 0.5 0.5]//Pe
ea=[1 1 1 1 1 1 0.5 3 5]//Pea
h=[1 3 5 1 3 3 5 3 1]//Ph
Z=[r;et;ea;h]
function e=fun1(Z,p)
    R=Z(1)
    ET=Z(2)
    EA=Z(3)
    H=Z(4)
    k=p(1)
    ka=p(2)
    ke=p(3)
    e=R-((k*ET*H)/(1+ka*EA+ke*ET))
endfunction
p0=[1;1;1]
[p,err]=datafit(fun1,Z,p0);
disp(p)

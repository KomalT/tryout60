clc;clear;
//Que 3 alg eqns
Q1=1//unit
//Q2=k(1)  Q3=k(2)  Q4=k(3)  Q5=k(4)  Q6=k(5)  Q7=k(6)
function f=Flow(k)
    f(1)=k(2)+2*k(3)-2*k(1);
    f(2)=k(4)+2*k(5)-2*k(3);
    f(3)=3*k(6)-2*k(5);
    f(4)=1-k(1)-k(2);
    f(5)=k(2)-k(3)-k(4);
    f(6)=k(4)-k(5)-k(6);
endfunction
k=[.5 .5 .5 .5 .5 .5]
y=fsolve(k,Flow)
disp(y)

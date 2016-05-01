clear;clc;
//que4
function f=H(t)
    f=50*(2.5*10^(-4)*t^4-10^(-2)*t^3-.2*t^2+3*t+.2);//kJ/m2h
endfunction
t=0:.5:10//h
y=intsplin(t,H(t));//kJ
disp(y)

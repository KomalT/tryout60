clc;clear;
//cA Vs t (que 3)
function f=cA(x)
    f=(2+.6*x.^1.6)./(1+.5*x.^.7);
endfunction
x=.2:.1:1
y=intsplin(x,cA(x))
disp(y)
//plot(x,cA(x))

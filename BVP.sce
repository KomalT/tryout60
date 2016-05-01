//BVP
clc;clear;
function [ydot]=f(t,y)
    ydot(1)=y(2);
    ydot(2)=2*y(1)^2+4*t*y(1)*y(2);
endfunction
a=0;
y0=[1/4,a]';
t0=0;
t=0:.1:1;
y=ode(y0,t0,t,f);
disp(y)

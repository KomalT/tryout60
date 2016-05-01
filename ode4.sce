clc;clear;
t=0.00001:.003:.5;
t0=0.00001;
y0=[.1;0];
function [ydot]=f(t,y)
    ydot(1)=y(2);
    ydot(2)=4*10^-6*y(1)-2*y(2)/t;
endfunction
  [y]=ode(y0,t0,t,f);
  disp(y)

clc;clear;
t=0:.5:7;
t0=0;
y0=[.95;.05;0];
function [ydot]=f(t,y)
    ydot(1)=-.08*y(1)^.5-2*y(1)^.2*y(2);
    ydot(2)=-3.5*10^(-6)*y(1)^.2+1.6*10^(-6)*y(3);
    ydot(3)=2*y(1)^.2*y(2)-.16*y(3)^.3;
endfunction
  [y]=ode(y0,t0,t,f);
  disp(y)

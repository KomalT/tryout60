clc;clear;
t=0:.25:3;//here y(1) is x y(2) is y
t0=0;
y0=[0;0];
function [ydot]=f(t,y)
    ydot(1)=3*t^2-.7*y(1);
    ydot(2)=.7*y(1)-.02*y(2);
endfunction
  [y]=ode(y0,t0,t,f);
  disp(y)
  for i=1:1:13
      x(i)=y(1,i);
      y(i)=y(2,i);
  end
//plot(t,x)
plot(t,y,'g')

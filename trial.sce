clc;clear;
x0=0;
y0=0;
x=0:.5:1
function ydot=f(x, y)
    ydot=x^2+y;
endfunction
 y=ode(y0,x0,x,f);
  disp(y)

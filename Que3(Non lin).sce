clc;clear;
//Volume
r=1//m
V=.75//m3
h=V/(3.14*r^2)//initial guess
function f=Volume(h)
    f=V-3.14*h^2*(3*r-h)/3;
endfunction
y=fsolve(h,Volume)
disp(y)//m

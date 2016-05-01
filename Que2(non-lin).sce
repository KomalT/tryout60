//RECYCLE
clc;clear;
xaf=.95
R1=.4
function [y]=Recycle(R)
    y(1)=log((1+R*(1-xaf))/(R*(1-xaf)))-((R+1)/(R*(1+R*(1-xaf))));
endfunction

y1 = fsolve(R1,Recycle);
disp(y1)//m3
//y2=Recycle(10)
//disp(y2)

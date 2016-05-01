//Since this was first program on fsolve it thought its unable to handle six eqns hence i converted them to 3 variables however i kept the initial comments to refer
clc;clear;
//distillation columns in series
//...comp    Feed  Stream1   Intemediates   Stream2    Stream3
//...Ethane.. 20   .94k(4)   k(1)           .01k(5)    .01k(6)
//...Propne.. 50   .05k(4)   k(2)           .96k(5)    .07k(6)
//...Butane.. 30   .01k(4)   k(3)           .03k(5)    .92k(6)
function [f]=Dist(k)
    f(1)=20-.94*k(1)-.01*k(2)-.01*k(3);
    f(2)=50-.05*k(1)-.96*k(2)-.07*k(3);
    f(3)=30-.01*k(1)-.03*k(2)-.92*k(3);
    //f(4)=k(1)-.01*k(5)-.01*k(6);//k(4)=stream1=k(1)
    //f(5)=k(2)-.96*k(5)-.07*k(6);//k(5)=stream2=k(2)
    //f(6)=k(3)-.03*k(5)-.92*k(6);//k(6)=stream3=k(3)
endfunction
k=[20 20 20]'//initial guess
y=fsolve(k,Dist);
disp(y)
e1=100-y(1)-y(2)-y(3);
disp(e1)
//e2=k(1)+k(2)+k(3)-k(5)-k(6);
//disp(e2)
//Int1=k(1)+k(2)+k(3)
//disp(Int1)
Str1=y(1)
disp(y(1))
str2=y(2)
disp(y(2))
str3=y(3)
disp(y(3))
Int1=(.01*y(2)+.01*y(3))/(y(2)+y(3));//comp of ethane in intermediate
disp(Int1)
Int2=(.96*y(2)+.07*y(3))/(y(2)+y(3));//comp of propane in intermediate
disp(Int2)
Int3=(.03*y(2)+.92*y(3))/(y(2)+y(3));//comp of butane in intermediate
disp(Int3)
//err2=1-Int1-Int2-Int3;
//disp(err2)

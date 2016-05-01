clc;clear;
//euler
t=0:.1:10;
T=100;
t=0;
Z=[T,t]
for i=1:1:100
 T(i+1)=T(i)+0.1*(-0.3*(T(i)-50)^1.25)
end
disp(T(101));
//rk
t=0:.1:10;
T0=100;
t0=0;
function ydot=f(t,y)
    ydot=-.3*(y-50)^1.25
endfunction
[y]=ode(T0,t0,t,f);
disp(y)
//analytical
function T1=f2(t)
    T1=50+(.075*t+.37605)^(-4)
endfunction
for i=1:1:101
    T1(i)=f2(t(i));
    Diff(i)=T1(i)-y(i);
end
disp(Diff)

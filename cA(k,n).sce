clc;clear;
//k n=k(2)
t=[10 20 30 40 50 60]
cA=[3.52 2.48 1.75 1.23 .87 .61]
plot(cA,t,'+')
cA0=3.52;
t0=10;
Z=[cA;t];
function cA=datafit1(t,k)
    cA=((k(2)-1)*k(1)*(t-t0)+cA0^(1-k(2)))^(1/(1-k(2)));
endfunction
k0=[1,10]'
for i=1:1:6
    y0(i)=datafit1(t(i),k0);
end
disp(y0)
function e=myerror(k,Z)
    cA=Z(1);t=Z(2);
    e=cA-datafit1(t,k)
endfunction
[k1,err]=datafit(myerror,Z,k0)
for i=1:1:6
    y0(i)=datafit1(t(i),k1);
end
disp(k1)
plot(y0,t,'b')
cA=cA0*exp(-k1(1)*t);
plot(cA,t,'g')

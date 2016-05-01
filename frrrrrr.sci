clc;clear;
x=[0 1 2 3];
y=[0 1 4 9];
Z=[x;y];
//disp(Z)
function y=datafit1(x,k)
    y=k*x^2;
endfunction
k=4;
for i=1:1:4
    yy(i)=datafit1(x(1,i),k);
end
//disp(yy)
function e = G(k,z)
    x=z(1);y=z(2);
    e=y-datafit1(x,k);
endfunction
[k,err]=datafit(G,Z,k)
disp(k)

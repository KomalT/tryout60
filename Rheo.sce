
clc;clear;
x=[0 .002 .006 .012 .018 .024]//m
v=[0 .287 .899 1.915 3.048 4.299]//m/s
Meu=1.8*10^(-5);
plot(x,v,'+')

Z=[x;v];
k0=170;
function v=datafit1(x,k)
    v=k*x;
endfunction
for i=1:1:6
    yy(i)=datafit1(x(i),k0);
end

function e = myerror(k,Z)
    x=Z(1);v=Z(2);
    e= v - datafit1(x,k);
endfunction
//disp(yy)
//for i=1:1:6
//    yy(i)=myerror(k0,Z);
//end
//disp(yy)
[k,err]=datafit(myerror,Z,k0);
disp(k)
disp(err)
for i=1:1:6
    yy(i)=datafit1(x(i),k);
end
plot(x,yy,'g')
x=0;
Tow0=Meu*derivative(datafit1,x)
disp(Tow0)

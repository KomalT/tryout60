clc;clear;
//For Re calc
D=.005//m
v=40//m/s
Ro=1.23//kg/m3
Meu=1.79*10^(-5)//N.s/m2
Re=D*v*Ro/Meu
disp(Re)
if Re<10^5 then
    f=.316/Re^.25
end
L=.2//m
deltaP=f*L*Ro*v^2/(2*D)
disp(deltaP)//Pa

E=.0015*10^(-3)
f1=.002//initial guess
function y= Fcole(f)
    y=1/f^.5+2*log(E/(3.7*D)+2.51/(Re*f^.5))/2.303
endfunction
f=fsolve(f1,Fcole)
disp(f)
L=.2//m
deltaP=f*L*Ro*v^2/(2*D)
disp(deltaP)//Pa

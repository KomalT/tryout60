clc;clear;
//calc of mole fraction from weight fraction
w=[.900 .850 .800 .750 .700 0.600 0.500 0.400 0.300 0.200 .015 .010]//weight fraction
m1=86.845//molecular wt of LiBr
m2=84.1157//molecular wt of HCOOK
m3=18//molecular wt of H2O
//calc 2w/3 w/3 (1-w)
N1=2*w/(3*m1);
N2=w/(3*m2);
N3=(1-w)/m3;
Ntotal=N1+N2+N3;
x1=N1./Ntotal;
x2=N2./Ntotal;
x3=N3./Ntotal;
xc1=x1./(x1+x2+1);
xa1=xc1;
xc2=x2./(x1+x2+1);
xa2=xc2;
xm=x3./(x1+x2+1);

//calculating VP
N=[0.11670521452767*(10^4),-724213.16703206,-17.073846940092,0.12020824702470*(10^5),-3232555.0322333,0.14915108613530*(10^2),-4823.2657361591,0.40511340542057*(10^6),-0.23855557567849,0.65017534844798*(10^3)]
T=333.15 //K
v=T+(N(1,9)/(T-N(1,10)))
A=v^2+N(1,1)*v+N(1,2)
B=N(1,3)*v^2+N(1,4)*v+N(1,5)
C=N(1,6)*v^2+N(1,7)*v+N(1,8)
VP=(2*C/(-B+(B^2-4*A*C)^0.5))^4 //MPa
disp(VP)
P=[5 7.5 8 8.3 9 10.2 10 11.7 13.6 15.3 16 17]
plot(xm,P,'+')
//DEBYE-HUCKEL PART
//1.gama calc
s=-61.4453*exp((T-273.15)/273.15)+2.864468*((exp((T-273.15)/273.15))^2)+183.379*log(T/273.15)-.6820223*(T-273.15)+.0007875695*(T^2-273.15^2)+58.95788*273.15/T;
I=(xc1+xc2+xa1+xa2)/2;
V=exp((sqrt(1000/18)*s*(2*I.^1.5./(1+14.9*I.^.5))));
//A(1)=T(c1a1,m)  t1=alpha(c1a1,m)  A(3)=T(c2a2,m)  t3=alpha(c2a2,m)
//A(2)=T(m,c1a1)  t2=alpha(m,c1a1)  A(4)=T(m,c2a2)  t4=alpha(m,c2a2)
//A(6)=T(m,c1a2)  t6=alpha(m,c1a2)  A(8)=T(m,c2a1)  t8=alpha(m,c2a1)
//A(5)=T(c1a2,m)  t1=alpha(c1a2,m)  A(7)=T(c2a1,m)  t7=alpha(c2a1,m)
//A(9)=T(a2c1,a1c1)  t9=alpha(a2c1,a1c1)  A(10)=T(a1c2,a2c2)  t10=alpha(a1c2,a2c2)
//-A(9)=T(a1c1,a2c1)  t9=alpha(a1c1,a2c1)  -A(10)=T(a2c2,a1c2)  t10=alpha(a2c2,a1c2)
//A(11)=T(c2a1,c1a1)  t11=alpha(c2a1,c1a1)  A(12)=T(c1a2,c2a2)  t12=alpha(c1a2,c2a2)
//-A(11)=T(c1a1,c2a1)  t11=alpha(c1a1,c2a1)  -A(12)=T(c2a2,c1a2)  t12=alpha(c2a2,c1a2)
Z=[xc1;xa1;xc2;xa2;xm;V;P];
A0=[-1.9 1.1 -.6 1.2 -1.6 1 -1.1 1.9 .6 -1.3 0 -.9]'
function y = datafit_1(xc1,xa1,xc2,xa2,xm,V,A)
    ya1=xa1/(xa1+xa2);
    ya2=xa2/(xa1+xa2);
    yc1=xc1/(xc1+xc2);
    yc2=xc2/(xc1+xc2);
    G1=ya1*exp(-.2*A(1))+ya2*exp(-.2*A(5));
    G2=ya1*exp(-.2*A(7))+ya2*exp(-.2*A(3));
    G3=yc1*exp(-.2*A(1))+yc2*exp(-.2*A(7));
    G4=yc1*exp(-.2*A(5))+yc2*exp(-.2*A(3));
    T1=-log(G1)/.2;
    T2=-log(G2)/.2;
    T3=-log(G3)/.2;
    T4=-log(G4)/.2;
    T111=T1+A(2)-A(1);
    T122=T2+A(4)-A(3);
    T112=T1+A(6)-A(5);
    T121=T2+A(8)-A(7);
    T211=T3+A(2)-A(1);
    T222=T4+A(4)-A(3);
    T221=T3+A(8)-A(7);
    T212=T4+A(6)-A(5);
    K1=(xa1*G3*T3+xc1*G1*T3+xa2*G4*T4+xc2*G2*T2)/(xm+xa1*G3+xc1*G1+xa2*G4+xc2*G2);
    K2=-xm*K1/(xm+xa1*G3+xc1*G1+xa2*G4+xc2*G2);
    K31=(xa1/(xa1+xa2)*(xc1*exp(-.2*T111))/(xa1+xa2*exp(-.2*A(9))+xm*exp(-.2*T111)));
    K32=T111-(xa2*exp(-.2*A(9))*A(9)+xm*exp(-.2*T111)*T111)/(xa1+xa2*exp(-.2*A(9))+xm*exp(-.2*T111));
    K3=K31*K32;
    K41=(xa2/(xa1+xa2)*(xc2*exp(-.2*T122))/(xa2+xa1*exp(-.2*A(10))+xm*exp(-.2*T122)));
    K42=T122-(xa1*exp(-.2*A(10))*A(10)+xm*exp(-.2*T122)*T122)/(xa2+xa1*exp(-.2*A(10))+xm*exp(-.2*T122));
    K4=K41*K42;
    K51=(xa2/(xa1+xa2)*(xc1*exp(-.2*T112))/(xa2+xa1*exp(.2*A(9))+xm*exp(-.2*T112)));
    K52=T112-(xm*exp(-.2*T112)*T112-xa1*exp(.2*A(9))*A(9))/(xa2+xa1*exp(A(9)*.2)+xm*exp(-.2*T112));
    K5=K51*K52;
    K61=(xa1/(xa1+xa2)*(xc2*exp(-.2*T121))/(xa1+xa2*exp(A(10)*.2)+xm*exp(-.2*T121)));
    K62=T121-(xm*exp(-.2*T121)*T121-xa2*exp(A(10)*.2)*A(10))/(xa1+xa2*exp(A(10)*.2)+xm*exp(-.2*T121));
    K6=K61*K62;
    K71=(xc1/(xc1+xc2)*(xa1*exp(-.2*T211))/(xc1+xc2*exp(-A(11)*.2)+xm*exp(-.2*T211)));
    K72=T211-(xc2*exp(-.2*A(11))*A(11)+xm*exp(-.2*T211)*T211)/(xc1+xc2*exp(-A(11)*.2)+xm*exp(-.2*T211));
    K7=K71*K72;
    K81=(xc2/(xc1+xc2)*(xa2*exp(-.2*T222))/(xc2+xc1*exp(-A(12)*.2)+xm*exp(-.2*T222)));
    K82=T222-(xc1*exp(-A(12)*.2)*A(12)+xm*exp(-.2*T222)*T222)/(xc2+xc1*exp(-A(12)*.2)+xm*exp(-.2*T222));
    K8=K81*K82;
    K91=(xc1/(xc1+xc2)*(xa2*exp(-.2*T212))/(xc1+xc2*exp(A(12)*.2)+xm*exp(-.2*T212)));
    K92=T212-(xm*exp(-.2*T212)*T212-xc2*exp(A(12)*.2)*A(12))/(xc1+xc2*exp(A(12)*.2)+xm*exp(-.2*T212));
    K9=K91*K92;
    K101=(xc2/(xc1+xc2)*(xa1*exp(-.2*T221))/(xc2+xc1*exp(A(11)*.2)+xm*exp(-.2*T221)));
    K102=T221-(xm*exp(-.2*T221)*T221-xc1*exp(A(11)*.2)*A(11))/(xc2+xc1*exp(A(11)*.2)+xm*exp(-.2*T221));
    K10=K101*K102;
    U=exp(K1+K2+K3+K4+K5+K6+K7+K8+K9+K10);
    y=1000*VP*xm*U*V;
endfunction

for i=1:1:12
yy(1,i)=datafit_1(xc1(1,i),xa1(1,i),xc2(1,i),xa2(1,i),xm(1,i),V(1,i),A0);
end
function e = myerror(A,z)
    xc1=z(1);xa1=z(2);xc2=z(3);xa2=z(4);xm=z(5);V=z(6);y=z(7);
    e= y - datafit_1(xc1,xa1,xc2,xa2,xm,V,A0);
endfunction
[A1,err]=datafit(myerror,Z,A0); 
disp(A1)
disp(err)
for j=1:1:12
yy2(1,j)=datafit_1(xc1(1,j),xa1(1,j),xc2(1,j),xa2(1,j),xm(1,j),V(1,j),A1);
end
plot(xm, yy2,'g');

















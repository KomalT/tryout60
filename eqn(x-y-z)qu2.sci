// que2 alg eqns
// x=k(1)  y=k(2)   z=k(3)
function [f]=eqn(k)
    f(1)=80*k(1)+30*k(3)-40;
    f(2)=80*k(2)+10*k(3)-27;
    f(3)=20*k(1)+20*k(2)+60*k(3)-30;
endfunction
k=[.5 .5 .5]
y=fsolve(k,eqn)
disp(y)
// By matrix 
A=[80 0 30;0 80 10;20 20 60]';
B=[40 27 33]';
y=A^(-1)*B;
disp(y)

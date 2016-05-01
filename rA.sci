clc;clear;//t=0:0.1:%pi
//intsplin(t,sin(t))
cA0=0.0625//M
function f=rA(x)
    f=(100*0.0625^(0.5)*(1+x)^0.5)./((1-x)^0.5)
endfunction
x=0:.1:.8
y=intsplin(x,rA(x))
disp(y)

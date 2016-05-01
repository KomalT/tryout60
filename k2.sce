P1s = 0.43596
P2s = 0.23738
x=[0:0.1:1];
P=P2s+((P1s-P2s)*x);
yrl=P1s*x./P ;
plot(x,yrl,'g')
xexp=[0 .0819 .2192 .3584 .3831 .5256 .8478 .9872 1]
yexp=[0 .1869 .4065 .5509 .5748 .6786 .8741 .9863 1]
plot(xexp,yexp,'+' )
Amar=0.5196743 
gama1=exp(Amar*(1-x)^2);
gama2=exp(Amar*x^2);
Pmar=(P1s*gama1.*x)+(P2s*gama2.*(1-x));
ymar=(P1s*gama1.*x)./Pmar;
plot(x,ymar,'b')

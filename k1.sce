P1s = 0.43596
P2s = 0.23738
x=[0:0.1:1];
P=P2s+((P1s-P2s)*x);
y=x*P1s ./P ;
plot(x,P,'b')
Amar=0.5196743 
gama1=exp(Amar*(1-x)^2);
gama2=exp(Amar*x^2);
Pmar=(P1s*gama1.*x)+(P2s*gama2.*(1-x));
ymar=(P1s*gama1.*x)./Pmar;
plot(x,Pmar,'g')
xexp=[.0819 .2192 .3584 .3831 .5256 .8478 .9872]
gmaexp1=[1.4187 1.3598 1.2773 1.2615 1.1714 1.021 1.00]
gmaexp2=[1.006 1.043 1.1052 1.1184 1.2033 1.3925 1.4342]
Pexp=(P1s*gmaexp1.*xexp)+(P2s*gmaexp2.*(1-xexp));
ymar=(P1s*gmaexp1.*xexp)./Pexp;
plot(xexp,Pexp,'+')
title("P Vs x","x","P");
legend("Prl","Pmar")

clc,clear,close all
f2=@(x,y)sqrt(1-x.^2-y.^2)
ymax2=@(x)sqrt(x-x.^2);
ymin2=@(x)-ymax2(x);
I2=integral2(f2,0,1,ymin2,ymax2)
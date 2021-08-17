clc,clear,close all
I1 = integral(@(x)1./(x.*(x.^2-3*x+2).^(1/3)),2,inf)
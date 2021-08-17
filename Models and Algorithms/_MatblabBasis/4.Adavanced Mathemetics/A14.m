clc,clear,close all
syms x
y=x^3+6*x^2+8*x-1;
dy=diff(y);
xx=solve(dy);
fplot(y)
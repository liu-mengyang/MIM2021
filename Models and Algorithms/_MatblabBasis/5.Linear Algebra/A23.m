clc,clear,close all
a=sym([1,1,0;1,0,1;1,1,1;1,2,-1]);
b=sym([1;2;0;-1]);
x=pinv(a)*b
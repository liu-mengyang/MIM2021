clc,clear,close all
a=sym([1,-1,-1,1;1,-1,1,-3;1,-1,-2,3]);
b=sym([0;1;-1/2]);
c=rref([a,b])
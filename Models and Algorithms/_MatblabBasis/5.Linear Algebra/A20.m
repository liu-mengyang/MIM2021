clc,clear,close all
a=sym([2,2,-1;2,-1,2;-1,2,2]);
b=sym([1,4;0,3;-4,2]);
c=rref([a,b])
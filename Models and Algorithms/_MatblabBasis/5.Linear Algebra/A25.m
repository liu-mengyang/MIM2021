clc,clear,close all
A=sym([0,1,1,-1;1,0,-1,1;1,-1,0,1;-1,1,1,0]);
[P1,D]=eig(A)
P2=orth(P1)
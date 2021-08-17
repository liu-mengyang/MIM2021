clc,clear,close all
syms x
dy=diff(log((x+2)/(1-x)),x,3)
dy=simplify(dy)
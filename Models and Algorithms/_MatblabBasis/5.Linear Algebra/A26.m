clc,clear,close all
a=[2,-2,0;-2,4,0;0,0,5];
b=eig(a)
if all(b>0)
	fprintf('yes\n')
else
	fprintf('no\n')
end
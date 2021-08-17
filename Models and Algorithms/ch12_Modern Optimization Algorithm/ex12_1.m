clc,clear,close all
% prepare location data
sj0 = load('data12_1.txt');
x = sj0(:,[1:2:8]);
x = x(:);   % flatten
y = sj0(:,[2:2:8]);
y = y(:);
sj = [x y];

% compute distance
d1 = [70, 40];  % start coordinate
xy = [d1;sj;d1];
sj = xy * pi / 180;
d = zeros(102);
for i = 1 : 102
    for j = i + 1 : 102
        d(i,j)=6370 * acos(cos(sj(i,1)-sj(j,1))*cos(sj(i,2))*cos(sj(j,2))+sin(sj(i,2))*sin(sj(j,2)));
    end
end
d=d+d';

% solve
path = [];
long = inf;
% random 1000 epochs to generate a well initial solve
for j = 1:1000
    path0 = [1 1+randperm(100), 102];
    temp = 0;
    for i = 1:101
        temp = temp + d(path0(i),path0(i+1));
    end
    if temp < long
        path = path0;
        long = temp;
    end
end

% simulated annealing
e=0.1^30;
L=20000;
at=0.999;
T=1;
for k=1:L
    % create new solve
    c=2+floor(100*rand(1,2));
    c=sort(c);
    c1=c(1);
    c2=c(2);
    % compute increment
    df=d(path(c1-1),path(c2))+d(path(c1),path(c2+1))-d(path(c1-1),path(c1))-d(path(c2),path(c2+1));
    if df<0
        path=[path(1:c1-1),path(c2:-1:c1),path(c2+1:102)];
        long=long+df;
    elseif exp(-df/T)>=rand
        path=[path(1:c1-1),path(c2:-1:c1),path(c2+1:102)];
        long=long+df;
    end
    T=T*at;
    if T<e
        break;
    end
end
time=long/1000;
path,long,time
xx=xy(path,1);
yy=xy(path,2);
plot(xx,yy,'-*')

    
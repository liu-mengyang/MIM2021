clc,clear,close all
tic     % count time start
sj0=load('data12_1.txt');
x=sj0(:,1:2:8);
x=x(:);
y=sj0(:,2:2:8);
y=y(:);
sj=[x y];
d1=[70,40];
xy=[d1;sj;d1];
sj=xy*pi/180;
d=zeros(102);
for i=1:101
    for j=i+1:102
        d(i,j)=6370*acos(cos(sj(i,1)-sj(j,1))*cos(sj(i,2))*cos(sj(j,2))+sin(sj(i,2))*sin(sj(j,2)));
    end
end
d=d+d';
w=50;
g=100;
for k=1:w
    c=randperm(100);
    c1=[1,c+1,102];
    for t=1:102
        flag=0;
        for m=1:100
            for n=m+2:101
                if d(c1(m),c1(n))+d(c1(m+1),c1(n+1))<d(c1(m),c1(m+1))+d(c1(n),c1(n+1))
                    c1(m+1:n)=c1(n:-1:m+1);
                    flag=1;
                end
            end
        end
        if flag==0
            J(k,c1)=1:102;
            break;
        end
    end
end
J(:,1)=0;
J=J/102;
for k=1:g   % Genetic Algorithm
    A=J;
    for i=1:2:w
        ch1(1)=rand; % generate chaos sequence
        for j=2:50
            ch1(j)=4*ch1(j-1)*(1-ch1(j-1)); % update chaos sequence
        end
        ch1=2+floor(100*ch1);   % select the point to cross
        temp=A(i,ch1);
        A(i,ch1)=A(i+1,ch1);    % cross
        A(i+1,ch1)=temp;
    end
    by=[];
    while ~length(by)
        by=find(rand(1,w)<0.1); % select the samples to variate
    end
    num1=length(by);
    B=J(by,:);
    ch2=rand;   % generate chaos sequence
    for t=2:2*num1
        ch2(t)=4*ch2(t-1)*(1-ch2(t-1)); % update chaos sequence
    end
    for j=1:num1
        bw=sort(2+floor(100*rand(1,2)));    % select the point to variate
        B(j,bw)=ch2([j,j+1]);   % variate
    end
    G=[J;A;B];
    [SG,ind1]=sort(G,2);
    num2=size(G,1);
    long=zeros(1,num2);
    for j=1:num2
        for i=1:101
            long(j)=long(j)+d(ind1(j,i),ind1(j,i+1));
        end
    end
    [slong,ind2]=sort(long);
    J=G(ind2(1:w),:);
end
path=ind1(ind2(1),:),flong=slong(1)
toc
xx=xy(path,1);
yy=xy(path,2);
plot(xx,yy,'-o')
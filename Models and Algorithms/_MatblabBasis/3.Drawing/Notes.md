# 3. 绘图

## 3.1 二维绘图

### 3.1.1 plot

使用线性坐标空间绘制图形。

提供了用于控制线色、数据点和线型的基本参数

```matlab
plot(x,y,'color_point_linestyle')
```

y与x均为向量，且具有相同的元素个数。

当x和y均为mxn矩阵时，plot命令将控制n条曲线。

线色（r-red,g-green,b-blue,w-white,k-black,m-magenta,c-cyan,y-yellow）

数据点(.,0,x,+,*,s,h,d,v,^,>,<,p)

线型(-,-.,--,:)

```matlab
plot(t,[x1,x2,x3])
```

多重曲线对应不同向量时

```matlab
plot(t1,x1,t2,x2,t3,x3)
```

#### 3.1.2 loglog

在两个对数坐标空间中绘制图形。

#### 3.1.3 semilogx

使用x轴（或y轴）为对数刻度，另外一个轴为线性刻度的坐标空间绘制图形。

#### 3.1.4 polarplot

使用极坐标空间绘制图形。

#### 3.1.5 subplot

`subplot`用于在屏幕上分开显示n个不同的坐标系，且可分别在每一个坐标系中绘制曲线。

```matplot
subplot(r,c,p)
```

将屏幕分成rxc个子窗口，p表示激活第p个子窗口。

#### 3.1.6 title

`title`命令用于在图中加入标题。

```matlab
title('My Title')
```

#### 3.1.7 xlabel

`xlabel`命令用于在图中加入x轴标题。

```matlab
xlabel('My X-axis Label')
```

#### 3.1.8 ylabel

`ylabel`命令用于在图中加入y轴标题。

```matlab
ylabel('My Y-axis Label')
```

#### 3.1.9 text

`text`命令用于在图中加入文字说明。

```matlab
text(x,y,'Text for annotation')
```

#### 3.1.10 gtext

`gtext`命令会使用鼠标定位文字注释的位置。

```matlab
gtext('Text for annotation').grid
```

#### 3.1.11 hold on

`hold on`是图形保持命令，用于将当前图形保持在屏幕上不变。

`hold off`解除保持。

`hold`用于转换保持状态。

## 3.2 显函数，符号函数或隐函数绘图

####  3.2.1 fplot

`fplot`命令用于绘制指定函数在某一区间的函数图。

```matlab
fplot(fun,lims)
```

绘制fun函数在x轴区间为limx=[xmin,xmax]的函数图，亦或者，x和y轴区间为lims=[xmin,xmax,ymin,ymax]的函数图。

#### 3.2.2 分段函数

```matlab
clc, clear, close all
fplot(@Afun1, [-3,3])
function y=Afun1(x);
y=(x+1).*(x<1)+(1+1./x).*(x>=1);
end
```

![image-20210730222349377](https://images.liumengyang.xyz/image-20210730222349377.png)

**匿名函数的形式**

```matlab
Afun2=@(x) (x+1)*(x<1)+(1+1/x)*(x>=1);
fplot(Afun2, [-3,3])
```

结果一致

#### 3.2.3 三角函数

```matlab
fplot(@(x)tan(x))
```

![image-20210730222835590](https://images.liumengyang.xyz/image-20210730222835590.png)

#### 3.2.4 椭圆

```matlab
xt=@(t)cos(t);
yt=@(t)2*sin(t);
fplot(xt,yt)
```

![image-20210730222957472](https://images.liumengyang.xyz/image-20210730222957472.png)

使用隐函数

```matlab
fimplicit(@(x,y)x.^2+y.^2/4-1)
```

与上次结果一致。

## 3.3 三维绘图

### 3.3.1 三维曲线

`plot3`和`fplot3`是三维曲线绘制命令，后者是使用函数画图。

`plot3(x,y,z)`通过描点连线画出曲线，它的参数都是n维向量。

```matlab
t=0:pi/50:10*pi;
subplot(121), plot3(sin(t),cos(t),t)
subplot(122), fplot3(@(t)sin(t),@(t)cos(t),@(t)t,[0,10*pi])
```

![image-20210730223527982](https://images.liumengyang.xyz/image-20210730223527982.png)

### 3.3.2 网格图

`mesh`和`fmesh`是三维网格图绘制命令。

`mesh(x,y,z)`画网格曲面，它的参数是同维数的数据矩阵，分别表示横坐标、纵坐标和竖坐标，它将数据点在空间中描出并连成网格。

绘制二元函数
$$
z=\frac{\sin(xy)}{xy}
$$
的三维网格图。

```matlab
clc,clear,close all
x=-5:0.2:5;
[x,y]=meshgrid(x);
z=(sin(x.*y)+eps)./(x.*y+eps);
subplot(121),mesh(x,y,z)
subplot(122),fmesh(@(x,y)sin(x.*y)./(x.*y))
```

![image-20210730223921216](https://images.liumengyang.xyz/image-20210730223921216.png)

### 3.3.3 表面图

`surf`和`fsurf`是绘制三维表面图的命令。

`surf(x,y,z)`画三维表面图，它的参数是同维数的数据矩阵。

同样绘制函数（1）。

```matlab
clc,clear,close all
x=-5:0.2:5;
[x,y]=meshgrid(x);
z=(sin(x.*y)+eps)./(x.*y+eps);
subplot(121),surf(x,y,z)
subplot(122),fsurf(@(x,y)sin(x.*y)./(x.*y))
```

![image-20210730224513559](https://images.liumengyang.xyz/image-20210730224513559.png)

### 3.3.4 旋转曲面

> 画出$x^2+(y-5)^2=16$​绕x轴旋转一周所形成的旋转曲面。

两种方法：

1. 直接使用隐函数画图
2. 转化为参数方程后画图

```matlab
clc,clear,close all
f=@(x,y,z)x.^2+(sqrt(y.^2+z.^2)-5).^2-16
subplot(121),fimplicit3(f,[-4,4,-9,9,-9,9])
x=@(u,v)4*cos(u);
y=@(u,v)(5+4*sin(u)).*cos(v);
z=@(u,v)(5+4*sin(u)).*sin(v);
subplot(122),fsurf(x,y,z)
```

![image-20210730225009251](https://images.liumengyang.xyz/image-20210730225009251.png)

### 3.3.5 二次曲面

#### 3.3.5.1 单页双曲面

$$
\frac{x^2}{4}+\frac{y^2}{10}-\frac{z^2}{8}=1
$$

同样是可以直接使用隐函数又或者转化为参数方程后画图。

```matlab
clc,clear,close all
f=@(x,y,z)x.^2/4+y.^2/10-z.^2/8-1;
subplot(121),fimplicit3(f,[-20,20,-20,20,-15,15])
x=@(u,v)2*cosh(v).*cos(u);
y=@(u,v)sqrt(10)*cosh(v).*sin(u);
z=@(u,v)2*sqrt(2)*sinh(v);
subplot(122),fmesh(x,y,z,[0,2*pi,-pi,pi])
```

![image-20210730225447300](https://images.liumengyang.xyz/image-20210730225447300.png)

#### 3.3.5.2 双叶双曲面

$$
\frac{x^2}{9}-\frac{y^2}{4}-z^2=1
$$

```matlab
f=@(x,y,z)x.^2/9-y.^2/4-z.^2-1;
fimplicit3(f)
```

![image-20210730225858404](https://images.liumengyang.xyz/image-20210730225858404.png)

#### 3.3.5.3 抛物柱面

$$
y^2=x
$$

```matlab
fsurf(@(y,z)y.^2)
```

![image-20210730225954391](https://images.liumengyang.xyz/image-20210730225954391.png)

#### 3.3.5.4 椭圆锥体

$$
\frac{x^2}{9}+\frac{y^2}{4}=z^2
$$

```matlab
subplot(121)
fimplicit3(@(x,y,z)x.^2/9+y.^2/4-z.^2,[-6,6,-4,4,-2,2])
subplot(122)
x=@(s,t)3*tan(s).*cos(t);
y=@(s,t)2*tan(s).*sin(t);
z=@(s,t)tan(s);
fsurf(x,y,z,[-1,1,0,2*pi])
```

![image-20210730230259846](https://images.liumengyang.xyz/image-20210730230259846.png)

#### 3.3.5.5 椭球面

$$
\frac{x^2}{9}+\frac{y^2}{4}+\frac{z^2}{6}=1
$$

椭球面有一个专门的函数可以绘制`ellipsoid`

```matlab
subplot(121)
fimplicit3(@(x,y,z)x.^2/9+y.^2/4+z.^2/6-1)
subplot(122)
ellipsoid(0,0,0,3,2,sqrt(6))
```

![image-20210730230433148](https://images.liumengyang.xyz/image-20210730230433148.png)

#### 3.3.5.6 马鞍面

$$
z=xy
$$

```matlab
fsurf(@(x,y)x.*y)
```

![image-20210730230513334](https://images.liumengyang.xyz/image-20210730230513334.png)

#### 3.3.5.7 椭圆柱面

$$
\frac{x^2}{9}+\frac{y^2}{4}=1
$$

```matlab
subplot(121), fimplicit3(@(x,y,z)x.^2/9+y.^2/4-1)
x=@(u,v)3*cos(u);
y=@(u,v)2*sin(u);
z=@(u,v)v;
subplot(122), fsurf(x,y,z)
```

![image-20210730230704108](https://images.liumengyang.xyz/image-20210730230704108.png)

### 3.3.6 其他

[略]

## 3.4 四维绘图

**isosurface**

```matlab
[x,y,z,v]=flow
isosurface(x,y,z,v)
```

![image-20210730230830457](https://images.liumengyang.xyz/image-20210730230830457.png)

**$v=x^2y(z+1)$**

```matlab
x=1:20;y=1:10;z=10:10;
[x,y,z]=meshgrid(x,y,z);
v=x.^2.*y.*(z+1);
isosurface(x,y,z,v)
```

![image-20210730231359310](https://images.liumengyang.xyz/image-20210730231359310.png)
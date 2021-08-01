# 4. 高等数学

## 4.1 求极限

`limit(expr, x, a)`表示求符号表达式`expr`关于符号变量`x`趋近于`a`时的极限，`limit(expr)`求默认变量趋近于0时的极限。

**求下列表达式的极限**
$$
\lim_{x\rightarrow0}\frac{\sqrt{1+x^2}-1}{1-\cos{x}}
$$

$$
\lim_{x\rightarrow+\infty}\lgroup1+\frac{a}{x}\rgroup^x
$$

```matlab
clc,clear,close all
syms x a
b1 = limit((sqrt(1+x^2)-1)/(1-cos(x)))
b2 = limit((1+a/x)^x, x, inf)
```

![image-20210801232317531](https://images.liumengyang.xyz/image-20210801232317531.png)

## 4.2 求导数

`diff`命令用于求导数，可以写成`diff(F,var,n)`或者`diff(F,var1,...,varN)`，表示求F关于变量var的n阶导数或者求关于变量var1,...,varN的N阶偏导数。当没有指定var时，默认为symvar(F,n)变量。

**求函数$y=\ln\frac{x+2}{1-x}$的三阶导数**

```matlab
clc,clear,close all
syms x
dy=diff(log((x+2)/(1-x)),x,3)
dy=simplify(dy)
```

![image-20210801233733779](https://images.liumengyang.xyz/image-20210801233733779.png)

其中`simplify`用于对符号函数进行化简

**求向量$a=\text{[0 0.5 2 4]}$的一阶差分**

```matlab
clc,clear,close all
a = [0,0.5,2,4];
da=diff(a)
```

![image-20210801233825942](https://images.liumengyang.xyz/image-20210801233825942.png)

## 4.3 求极值

通过`solve`命令可以对方程进行求解，对求导后的方程进行求解即可得到极值点和极值

**求函数$f(x)=x^3+6x^2+8x-1$的极值点，并画出函数的图形**

```matlab
clc,clear,close all
syms x
y=x^3+6*x^2+8*x-1;
dy=diff(y);
xx=solve(dy);
fplot(y)
```

![image-20210801234048829](https://images.liumengyang.xyz/image-20210801234048829.png)

## 4.4 求积分

### 4.4.1 不定积分

通过`int(expr,v)`求不定积分，参数含义与`diff`类似。

**求不定积分$\int{\frac{1}{1+\sqrt{(1-x^2)}}dx}$**

```matlab
clc,clear,close all
syms x
I=int(1/(1+sqrt(1-x^2)))
```

![image-20210802000229752](https://images.liumengyang.xyz/image-20210802000229752.png)

### 4.4.2 定积分



##### （1） 符号解

求定积分符号解仍然使用`int`命令，但可以增加两个参数指定上下限。

**求定积分$\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\cos{x}\cos{2x}dx$**

```matlab
clc,clear,close all
syms x
I=int(cos(x)*cos(2*x),-pi/2,pi/2)
```

![image-20210802000522588](https://images.liumengyang.xyz/image-20210802000522588.png)

##### （2）数值解

数值解使用`integral`命令求解

**求下列积分的数值解：**
$$
\int_2^{+\infty}\frac{dx}{x\cdot\sqrt[3]{x^2-3x+2}}
$$

```matlab
clc,clear,close all
I1 = integral(@(x)1./(x.*(x.^2-3*x+2).^(1/3)),2,inf)
```

![image-20210802000942308](https://images.liumengyang.xyz/image-20210802000942308.png)
$$
\iint\limits_D\sqrt{1-x^2-y^2}d\sigma,D=\{(x,y)|x^2+y^2\le x\}
$$

```matlab
clc,clear,close all
f2=@(x,y)sqrt(1-x.^2-y.^2)
ymax2=@(x)sqrt(x-x.^2);
ymin2=@(x)-ymax2(x);
I2=integral2(f2,0,1,ymin2,ymax2)
```

![image-20210802001315187](https://images.liumengyang.xyz/image-20210802001315187.png)
$$
\iiint\limits_\Omega\frac{z^2\ln{(x^2+y^2+z^2+1)}}{x^2+y^2+z^2+1}dv,\Omega={(x,y,z)|0\le z\le\sqrt{1-x^2-y^2}}
$$

```matlab
clc,clear,close all
f3=@(x,y,z)z.^2.*log(x.^2+y.^2+z.^2+1)./(x.^2+y.^2+z.^2+1);
ymax3=@(x)sqrt(1-x.^2);
ymin3=@(x)-ymax3(x);
zmax3=@(x,y)sqrt(1-x.^2-y.^2);
I3=integral3(f3,-1,1,ymin3,ymax3,0,zmax3)
```

![image-20210802001655133](https://images.liumengyang.xyz/image-20210802001655133.png)

## 4.5 级数求和

使用`symsum(expr,v,a,b)`命令进行级数求和

**求如下级数的和：**
$$
\sum\limits_{n=1}^{\infty}\frac{2n-1}{2^n}
$$

```matlab
clc,clear,close all
syms n
f1=(2*n-1)/2^n;
s1=symsum(f1,n,1,inf)
```

![image-20210802001949843](https://images.liumengyang.xyz/image-20210802001949843.png)
$$
\sum\limits_{n=1}^\infty\frac{1}{n^2}
$$

```matlab
clc,clear,close all
syms n
f2=1/n^2;
s2=symsum(f2,n,1,inf)
```

![image-20210802002103062](https://images.liumengyang.xyz/image-20210802002103062.png)
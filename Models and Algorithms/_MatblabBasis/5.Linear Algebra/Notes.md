# 5. 线性代数

## 5.1 向量组的线性相关性

通过`rref(A)`命令可以将A化成最简形，而最简形中单位向量对应的列向量即为最大线性无关组所含向量，其他列向量的坐标即为其对应向量用最大线性无关组线性表示的系数。

**求下列矩阵列向量组的一个最大无关组**
$$
\mathbf{A}=
\left[
\begin{matrix}
1 & -2 & -1 & 0 & 2\\
-2 & 4 & 2 & 6 & -6\\
2 & -1 & 0 & 2 & 3\\
3 & 3 & 3 & 3 & 4\\
\end{matrix}
\right]
$$

```matlab
clc,clear,close all
a=sym([1,-2,-1,0,2;-2,4,2,6,-6;2,-1,0,2,3;3,3,3,3,4]);
b=rref(a)
```

![image-20210804153456227](https://images.liumengyang.xyz/image-20210804153456227.png)

**设$A=[a_1,a_2,a_3]=\left[\begin{matrix}2 & 2 & -1\\2 & -1 & 2\\-1 & 2 & 2\end{matrix}\right],B=[b_1,b_2]=\left[\begin{matrix}1 & 4\\0 & 3\\-4 & 2\end{matrix}\right]$，验证$a_1,a_2,a_3$是$R^3$的一个基，并把$b_1,b_2$用这个基线性表示​​。**

通过求A与B拼接矩阵的最大无关组，若其中$a_1,a_2,a_3$​均为基向量则认为它们是一个基，同时也可以找到剩余向量的基线性表示。

```matlab
clc,clear,close all
a=sym([2,2,-1;2,-1,2;-1,2,2]);
b=sym([1,4;0,3;-4,2]);
c=rref([a,b])
```

![image-20210804154251253](https://images.liumengyang.xyz/image-20210804154251253.png)

## 5.2 齐次线性方程组

通过`null(A)`命令可以求矩阵$Ax=0$的解空间，即一组基。

当A为数值矩阵时，返回的列向量为方程组的正交规范基；

当A为符号矩阵时，返回的列向量为方程组的符号基础解系。

**求方程组的通解**
$$
\begin{cases}
x_1+2x_2+2x_3+x_4=0,\\
2x_2+x_2-2x_3-2x_4=0,\\
x_1-x_2-4x_3-3x_4=0.
\end{cases}
$$

```matlab
clc,clear,close all
a=sym([1,2,2,1;2,1,-2,-2;1,-1,-4,-3]);
b=null(a)
```

![image-20210804155843488](https://images.liumengyang.xyz/image-20210804155843488.png)

## 5.3 非齐次线性方程组

使用符号`\`求解非齐次线性方程组。这一符号内部实际是很复杂的求解算法（求解欠定方程组）。

也可以使用`rref(A)`求出最简形，即基础解系。

**求超定方程组**
$$
\begin{cases}
2x_1+4x_2=11,\\
3x_1-5x_2=3,\\
x_1+2x_2=6,\\
2x_1+x_2=7
\end{cases}
$$

```matlab
clc,clear,close all
a=[2,4;3,-5;1,2;2,1];
b=[11;3;6;7];
s=a\b
```

其实使用`pinv`也可以代替`\`，这是一个伪逆命令，它的使用范围更加广泛。当a列不满秩时，`\`无法使用，此时就必须`pinv(a)*b`。

![image-20210804160543956](https://images.liumengyang.xyz/image-20210804160543956.png)

**求下列方程组的最小二乘符号解**
$$
\begin{cases}
x_1+x_2=1,\\
x_1+x_3=2,\\
x_1+x_2+x_3=0,\\
x_1+2x_2-x_3=-1.
\end{cases}
$$

```matlab
clc,clear,close all
a=sym([1,1,0;1,0,1;1,1,1;1,2,-1]);
b=sym([1;2;0;-1]);
x=pinv(a)*b
```

![image-20210804160736174](https://images.liumengyang.xyz/image-20210804160736174.png)

**求解方程组**
$$
\begin{cases}
x_1-x_2-x_3+x_4=0,\\
x_1-x_2+x_3-3x_4=1,\\
x_1-x_2-2x_3+3x_4=-\frac{1}{2}
\end{cases}
$$

```matlab
clc,clear,close all
a=sym([1,-1,-1,1;1,-1,1,-3;1,-1,-2,3]);
b=sym([0;1;-1/2]);
c=rref([a,b])
```

![image-20210804161022067](https://images.liumengyang.xyz/image-20210804161022067.png)

## 5.4 相似矩阵及二次型

`eig`命令可以对矩阵进行相似对角化，`orth`命令可以对矩阵进行正交规范化。

**求一个正交变换$x=Py$，把二次型化为标准型**
$$
f=2x_1x_2+2x_1x_3-2x_1x_4-2x_2x_3+2x_2x_4+2x_3x_4\\
\mathbf{A}=
\left[
\begin{matrix}
0 & 1 & 1 & -1\\
1 & 0 & -1 & 1\\
1 & -1 & 0 & 1\\
-1 & 1 & 1 & 0
\end{matrix}
\right]
$$

```matlab
clc,clear,close all
A=sym([0,1,1,-1;1,0,-1,1;1,-1,0,1;-1,1,1,0]);
[P1,D]=eig(A)
P2=orth(P1)
```

![image-20210804163011668](https://images.liumengyang.xyz/image-20210804163011668.png)

**判别二次型$f=2x_1^2+4x_2^2+5x_3^2-4x_1x_2$的正定性**

```matlab
clc,clear,close all
a=[2,-2,0;-2,4,0;0,0,5];
b=eig(a)
if all(b>0)
	fprintf('yes\n')
else
	fprintf('no\n')
end
```

![image-20210804163219781](https://images.liumengyang.xyz/image-20210804163219781.png)


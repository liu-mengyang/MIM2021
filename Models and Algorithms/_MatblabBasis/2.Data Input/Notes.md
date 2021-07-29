# 2. Data Input

## 1. 矩阵输入

### 1. 直接输入

```matlab
A=[1,2,3;4,5,6;7,8,9]
```

![image-20210729161647930](https://images.liumengyang.xyz/image-20210729161647930.png)

矩阵变量会被保存在工作区，可被重新赋值，或者通过`clear`指令清楚，直到指令窗被关闭它都会一直存在。

### 2. 分行输入

```matlab
A=[1,2,3
   4,5,6
   7,8,9]
```

![image-20210729162615305](https://images.liumengyang.xyz/image-20210729162615305.png)

通过分行输入可以不用通过分号进行矩阵不同行的区分。

## 2. 特殊变量

### 1. ans

结果的默认变量名。

![image-20210729162856072](https://images.liumengyang.xyz/image-20210729162856072.png)

### 2. pi

圆周率。

![image-20210729162909361](https://images.liumengyang.xyz/image-20210729162909361.png)

### 3. eps

浮点相对精度。

![image-20210729162928245](https://images.liumengyang.xyz/image-20210729162928245.png)

### 4. inf

无穷大。

![image-20210729162949289](https://images.liumengyang.xyz/image-20210729162949289.png)

### 5. NaN

不定量（not a number）

![image-20210729163006850](https://images.liumengyang.xyz/image-20210729163006850.png)

### 6. i(j)

单位虚数

![image-20210729163236516](https://images.liumengyang.xyz/image-20210729163236516.png)

### 7. nargin

所用函数的输入变量数目。

### 8. nargout

所用函数的输出变量数目。

### 9. realmin

最小不可用实数。

![image-20210729163446113](https://images.liumengyang.xyz/image-20210729163446113.png)

### 10. realmax

最大不可用实数。

![image-20210729163501593](https://images.liumengyang.xyz/image-20210729163501593.png)

## 3. 特殊向量和特殊矩阵

### 1. 特殊向量

#### 1. 固定间隔行向量

```matlab
t=[0:0.1:10]
```

![image-20210729164051479](https://images.liumengyang.xyz/image-20210729164051479.png)

#### 2. 线性均匀分布向量

```matlab
t=linspace(0,10,20)
```

![image-20210729164143906](https://images.liumengyang.xyz/image-20210729164143906.png)

#### 3. 按照对数距离等间距向量

```matlab
t=logspace(0,10,30)
```

![image-20210729164247582](https://images.liumengyang.xyz/image-20210729164247582.png)

### 2. 特殊矩阵

#### 1. 单位矩阵

```matlab
eye(2)
```

![image-20210729164621474](https://images.liumengyang.xyz/image-20210729164621474.png)

```matlab
eye(2,3)
```

![image-20210729164645150](https://images.liumengyang.xyz/image-20210729164645150.png)

#### 2. 全1矩阵

```matlab
ones(2)
```

![image-20210729164741913](https://images.liumengyang.xyz/image-20210729164741913.png)

```matlab
ones(2,3)
```

![image-20210729164806361](https://images.liumengyang.xyz/image-20210729164806361.png)

#### 3. 全0矩阵

```matlab
zeros(2)
```

![image-20210729164853593](https://images.liumengyang.xyz/image-20210729164853593.png)

```matlab
zeros(2,3)
```

![image-20210729164904647](https://images.liumengyang.xyz/image-20210729164904647.png)

#### 4. 空矩阵

```matlab
q=[]
```

![image-20210729165139973](https://images.liumengyang.xyz/image-20210729165139973.png)

#### 5. 随机数矩阵

0-1均匀分布

```matlab
rand(3,2)
```

![image-20210729165246623](https://images.liumengyang.xyz/image-20210729165246623.png)

均值为mu，标准差为sigma的正态分布

```matlab
normrnd(mu,sigma,3,2)
```

![image-20210729165411914](https://images.liumengyang.xyz/image-20210729165411914.png)

均值为mu的指数分布

```matlab
exprnd(mu,3,2)
```

![image-20210729165538134](https://images.liumengyang.xyz/image-20210729165538134.png)

均值为mu的泊松分布

```matlab
poissrnd(mu,3,2)
```

![image-20210729165635592](https://images.liumengyang.xyz/image-20210729165635592.png)

均匀分布

```matlab
unifrnd(0,1,3,2)
```

![image-20210729165712638](https://images.liumengyang.xyz/image-20210729165712638.png)

#### 6. 随机置换

产生1~n的随机全排列

```matlab
randperm(n)
```

![image-20210729170036484](https://images.liumengyang.xyz/image-20210729170036484.png)

产生1~n的所有全排列

```matlab
perms([1:n])
```

![image-20210729170112419](https://images.liumengyang.xyz/image-20210729170112419.png)


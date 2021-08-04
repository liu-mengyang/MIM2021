# 6. 数据处理

## 6.1 mat文件

**mat保存**

通过`save`命令可以保存数据为mat文件

```matlab
a=1;
b=2;
c=3;
save dataA_27.mat a b c
```

![image-20210804175835311](https://images.liumengyang.xyz/image-20210804175835311.png)

**mat读取**

通过`load`命令可以读取mat文件中的数据

```matlab
load('dataA_27.mat')
```

![image-20210804175916344](https://images.liumengyang.xyz/image-20210804175916344.png)

## 6.2 文本文件

**加载文本文件数据**

通过`load`或`readmatrix`命令可以加载文本文件到工作空间（整行整列的数据）

![image-20210804180102211](https://images.liumengyang.xyz/image-20210804180102211.png)

```matlab
clc,clear,close all
a=load('dataA_29.txt')
b=readmatrix('dataA_29.txt')
```

![image-20210804180307470](https://images.liumengyang.xyz/image-20210804180307470.png)

**保存矩阵到文本文件**

通过命令`writematrix`可以实现保存矩阵到文本文件

```matlab
clc,clear,close all
b=randi([0,10],3)
writematrix(b,'dataA_30.txt')
```

![image-20210804180437207](https://images.liumengyang.xyz/image-20210804180437207.png)

这一命令同样可以保存到Excel文件

```matlab
clc,clear,close all
a=normrnd(0,1,100,200);
writematrix(a,'dataA_31.xlsx')
```

![image-20210804180614755](https://images.liumengyang.xyz/image-20210804180614755.png)

## 6.3 Excel文件

**保存数据**

`writematrix`命令在保存数据到Excel文件时，可以指定表单和域

```matlab
clc,clear,close all
a=rand(5,10);
warning('off')
writematrix(a,'dataA_32.xlsx','Sheet',2,'Range','B2')
```

![image-20210804180744080](https://images.liumengyang.xyz/image-20210804180744080.png)

**数据读取**

`readmatrix`命令可以读取指定区域的数据

```matlab
clc,clear,close all
b=readmatrix('dataA_32.xlsx','Sheet',2,'Range','C3:F6')
```

![image-20210804180913538](https://images.liumengyang.xyz/image-20210804180913538.png)

## 6.4 字符串数据

[略]

## 6.5 图像文件

[略]

## 6.6 批处理

[略]

## 6.7 时间序列数据

[略]

## 6.8 日期和时间

[略]

## 6.9 视频文件

[略]


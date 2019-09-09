#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/4'
# 求出1+2+3.....+100的和
a=0
for i in range(1,101):
     a=a+i
print(a)

# 求出100! 1*2*3*4....*100
s = 1
for i in range(1,101):
    s *= i
print(s)


for divisor in range(101):
    # range(x) 是 0到x-1 的list 数组
    if divisor < 3:
        # 1 和 2 这两个数先打印出来， 下面的判断直接从 3 开始
        print(divisor)
    else:
        for dividend in range(2, divisor+1):
            # 思路： 用我们取到的数 除以所有比他小的整数， 如果可以整除 则排除这个数是素数的可能性
            result = divisor%dividend
            if result == 0:
                # 可以整除的条件下 判断除数 是不是 等于 被除数，不等于则跳过
                if dividend != divisor:
                    break
                else:
                    #打印正确的结果
                    print(divisor)
for i in range (1,100):
   if(i % 2 == 1):
       print(i)
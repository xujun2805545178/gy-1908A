#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/5'
'''GET https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1'''
a="GET https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1"
l=a.split(" ")
print(l)
qqdz =l[2]
print("协议版本:" + qqdz)
q = l[0]
print("请求方法:" + q)
e = l[1]
o =e.split("?")
p =o[1]
print("请求数据:" + p)
u =e.split("://")
t =u[0]
print("协议:" + t)
i =e.split("/")
j =i[2]
print("ip:" + j)
k =i[3]
print("地址:" + k)




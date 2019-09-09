#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/6'

d = {}
dl = {"name":'夏末',"sex":'男'}
#新增一对数据
dl['age'],dl['id'] = 18,1
print(dl)
print(dl.pop('sex'))
del dl['age']
print(dl)
#del dl
#print(dl)
#dl.clear()
#dl = {}
dl = {"name":'夏末',"sex":'男'}
dl["name"] = '魏无羡'
print(dl)


d2 = {"1":'123',"2":'345'}
d3 = {"3":'124',"4":'8210'}
c = dict(d2,**d3)
print(c)


def aks():
    print("广大牛多个我阿里咖喱咖喱饭")


class ClassDemo1():
    def class_method_1(self):
        print("咖喱刚不过分了")

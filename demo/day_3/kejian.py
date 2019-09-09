#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/6'
'''
project 项目
package 包
module  模块
class 类
method 方法
'''
'''
列表中元素可被更改，元祖中元素不可更改
元祖中只有一个数据的时候需要以逗号结尾，列表不需要
'''
'''
字典:key:value
key唯一
key必须是不可变的，数字，字符串，元祖，列表（不可以），字典（不可以）
#增
#初次创建
d = {}
dl = {"name":'夏末'，"sex":'男'}
#新增一对数据
dl['age'] = 18
print(dl)
#删除key
print(dl.pop('sex'))
del dl['age']
print(dl)
#删除整个字典
del dl
print(dl)
#清空
dl.clear()
dl = {}
#改
dl["name"] = '魏无羡'
print(dl)
#有key就改key没有就加一个
#成员判断
print（"key" in dl）
#字典拼接
d2 = {"1":'123',"2":'345'}
d3 = {"3":'124',"4":'8210'}
#在某个字典末尾加上另一个字典
#拿着d3修改d2，key有则改key，没有就会新增
d2.update(d3)
print(d2)
#生成一个新的字典
print（dict(d2,**d3)）
#封装
类名+alt+回车
from demo.day_3.abjkc import aks
#类的封装
class ClassDemo1():
def class_method_1(self):
print("咖喱刚不过分了")
deme_1 = ClassDemo1()
deme_1.class_method_1()
'''
'''
自定义模块
复制到项目里边
然后在使用import 语法导入
使用

python 提供的内置模块
直接import导入
使用

第三方模块
'''
'''
#随机取数
import random
sun = random.randint(0,99)随机取*-*的数
sun = random.choice([0,99])随机取给定的数
'''
'''
a = 1
print("sss")
作用，输入到控制台
参数：要打印的对象，end修改结尾符号
type(a)
作用，返回变量类型
参数：变量
b = '1111'
len(b)
作用：查看str list tuple dict长度
参数：
str()
作用：把变量从其他类型转换为整形
参数：要转换的变量
list()
作用：把变量从其他类型转换为列表类型
参数：要转换的变量
dict()
作用：合并两个字典，生成一个新的字典
参数1：字典变量1
参数2：**字典变量2
tuple()
作用：把变量从其他类型转换为元祖类型
参数：要转换的变量
'''
'''打开读取
打开一个文件
参数1：文件路径
参数2：打开方式，r度w先清空文件内容，然后再写入a可读可写
f =open("test.txt","r")
按行读取文件内容，返回一个列表
print(f.readlines())
读取文件所有内容，返回一个字符串
print(f.read())
关闭
f.lose()
写入
f.write("......")
f.writelines(["alhahf\n",'glqihql\n','ao;va\n'])
\n换行符
'''
'''import os
dirs = os.listdir(".../day_3")
print(dirs)
print(os.path,join(".../day_3","fc.py"))
print(os.path.abspath("test.txt"))
p = os.path.abspath("test.txt")
print(os.path.dirname(p)
print(os.system("fc.py"))

'''
'''import time获取时间，格式化时间
print(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
'''
'''import re正则模块
a = "ailhdw1i231eajhndklads"
r = "([\d]+)"
rc=re.compile(r)
l=rc.findall(a)
print(l)
'''
'''
安装第三方包
1:下载并解压
cmd中切换目录至文件夹
执行命令 python setup.py install
install安装  uninstall卸载
2:pip工具
pip install 
3:pycharm中可用
file->settings->interpector->点+号->搜索要安装的包名->install Package 
'''
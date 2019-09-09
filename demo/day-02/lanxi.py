#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/5'
i = 1
while(i < 101):
    print(i)
    i +=1
def wu_can_shu(a,b):
    print(a+b)

wu_can_shu(10,40)

def asd(*args,**kwargs):
    print(args)
    print(kwargs)
asd({'name':'夏末'},1,2,3,0,2,1,7,2,7,0,a=10,b=120)

def ads(a,n=10):
    return a/n
print(ads(10))
print(ads(10,4))
print(ads(a=100,n=1000))

class Kei_Su_Lu():
    def kei(self):
        print('克总无线触须')
    def su(self):
        print('侦查员惨遭爆菊')
        self.kei()
if __name__== "__main__":
    c = Kei_Su_Lu()
    c.kei()
    c.su()
#dergakio   要求生成两个新的字符串  drai  和egko
a ='dergakio'
print(a[::2])
print(a[1::2])
#aderghij   要求生成两个新的字符串  aegi  和drhj
b='aderghij'
print(b[::2])
print(b[1::2])

c='打打架,交接,爱的回归'
print(c.split(','))


t='        打打架,交接,爱的回归         '
print(t.lstrip())
print(t.rstrip())


t='打打架,交接,            "爱的回归" '
print(t.replace(" ",''))
print(t.replace('"',"'"))
t=[1,2,3,4,5,6]
t.append(19)
print(t)
z=[1,2,3,4,5,6]
z.extend(t)
print(z)
x=[1,2,3,4,5,6]
x.insert(3,1111)
print(x)
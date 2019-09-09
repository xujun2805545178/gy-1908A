#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/4'

# 侦查员夏末调查奥法里尔镇人口失踪
import random
sun = random.randint(0,99)# 1=侦查员夏末成功调查处小镇人员失踪原因0=侦查员夏末sun值掉落到1，发疯投入克苏鲁的邪教怀抱
def wu_can_shu():
    a = 100
    sum = random.randint(0, 99)
    return a-sum
sun = wu_can_shu()
if(sun >=60):
    print("侦查员夏末成功调查处小镇人员失踪原因")
elif(sun > 30<60)   :
    print("侦查员夏末看见了不可理解之物陷入疯狂,神志不清")
else:
    print("侦查员夏末sun值掉落到1，发疯投入克苏鲁的邪教怀抱")

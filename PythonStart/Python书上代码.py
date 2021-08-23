# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 08:41:08 2019

@author: LCX
"""

str = "人生苦短m"
length1 = len(str.encode())
length2 = len(str.encode('gbk')) 
print("采用Python默认的编码方式（UTF-8）：" + str(length1) + "--采用gbk编码方式：" + str(length2))

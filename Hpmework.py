# -*- coding: utf-8 -*-
from math import sqrt
a = map(sqrt,[1,4,9,16,25])
print(a)

b = ['John', 'Paul', 'George', 'Ringo']
c = []
if 'John' in b or 'Paul' in b:
    if 'John' in b:
        c.append('John')
    if 'Paul' in b:
        c.append('Paul') 
print(c)
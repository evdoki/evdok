# -*- coding: utf-8 -*-
a = input()
summ = 0
for i in a:
    if int(i)%2 != 0:
        summ += int(i)**2
print(summ)
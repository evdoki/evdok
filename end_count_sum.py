# -*- coding: utf-8 -*-
summ = 0
while True:
    a = input()
    if a.isdigit:
        summ += int(a)
    elif a == 'stop':
        break
    else:
        continue
print(summ)
# -*- coding: utf-8 -*-
number = input()
number = number.split
summ = 0
for i in range(len(number)):
    if int(number[i])%2 != 0:
        summ += int(number[i])**2
print(summ)

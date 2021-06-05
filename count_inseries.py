# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 18:43:08 2016

@author: Sergiokapone

Програма розраховує кількість вказаних цифр в числах від n1 до n2 
"""

numeral = '6'
n1 = 1
n2 = 176
#lst = list(filter(lambda y: any(char == numeral for char in y), [str(x) for x in range(1,100)]))


lst = list(
           filter(
                  lambda y: any(char == numeral for char in y),
                  [item for sublist in
                  [str(x) for x in range(n1,n2+1)]
                  for item in sublist])
           )

print(len(lst))
n = 0
for num in range(len(lst)):
    n += lst[num].count(numeral)

print('Всього циферок', numeral,': ', n, 'штукенцій')


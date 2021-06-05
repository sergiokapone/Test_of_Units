# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 18:43:08 2016

@author: Sergiokapone

Функція get_num_count розраховує кількість вказаних цифр {numeral} в числах від {n1} до {n2} 
"""
def get_num_count(numeral, n1, n2):
    numeral_str = str(numeral)
    lst = list(
                filter(
                    lambda y: any(char == numeral_str for char in y),
                    [item for sublist in
                        [str(x) for x in range(n1,n2+1)]
                    for item in sublist]
                    )
              )
    return len(lst)
    
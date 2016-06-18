#!/usr/bin/env python
# coding=utf-8

import random

def parking(low, heigh):
    if heigh - low < 1:
        return 0
    else:
        x = random.uniform(low, heigh - 1)
        return 1 + parking(low, x) + parking(x+1, heigh)

print parking(0, 9)



# 阶乘

def p(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*p(n-1)

print  p(10)

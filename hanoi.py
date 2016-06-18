#!/usr/bin/env python
# coding=utf-8

count = 0

def hanoi(n, a = 'lift', b = 'mid', c = 'right'):
    global count
    if 1 == n:
        format = 'Move %3d from %5s to %5s count: %i'
        count += 1
        print format % (n, a, c, count)
    else:
        hanoi(n-1, a, c, b)
        format = 'Move %3d from %5s to %5s count : %i'
        count += 1
        print format % (n, a, c, count)
        hanoi(n-1, b, a, c)

hanoi(4)

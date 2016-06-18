#!/usr/bin/env python
# coding=utf-8

def is_panlindrom_rec(arg):
    if len(arg) <= 1:
        print 1
        return True
    else:
        if arg[0] != arg[-1]:
            return False
        else:
            return is_panlindrom_rec(arg[1: -1])


is_panlindrom_rec('1221')

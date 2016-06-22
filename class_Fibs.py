#!/usr/bin/env python
# coding=utf-8

class Fibs():
    
    def __init__(self):
        self.a = 0
        self.b = 1
    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
    def __iter__(self):
        return self

f = Fibs()
fa = []
fb = []
for i in range(9):
    fa.append(f.next())
    #print(f.next())
fa
for i in range(5):
    fb.append(f.next())
fb


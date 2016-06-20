#!/usr/bin/env python
# coding=utf-8

with open('/proc/meminfo') as fd:
    if line.startswith('meminfo'):
        total = line.split()[1]
    if line.startswith('MemFree'):
        free = line.split()[1]
print total, free

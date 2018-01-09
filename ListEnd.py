#!/usr/bin/env python

def list_end(lst):
    return[lst[0], lst[len(lst)-1]]

a = [5, 10, 15, 20, 25]
b = list_end(a)
print(b)

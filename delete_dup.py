#!/usr/bin/env python
import sys

fread = open('1.txt','r')
fwrite = open('11.txt','w')

s = set()

for i in fread:
    s.add(i)

for i in s:
    fwrite.write(i)

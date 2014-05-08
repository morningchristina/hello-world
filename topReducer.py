#!/usr/bin/env python
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
result = {}
fread = open('aftersort.txt','r')
for lines in fread:
    lines = lines.strip()
    lines = lines.decode('utf-8')
    word = lines.split()[0]
    count = lines.split()[1]
    result.setdefault(word,count)
    key = result.keys()
    value = result.values()
    value.sort()
    print value 

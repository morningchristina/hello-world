#!/usr/bin/env python

import sys

fread = open('result1.txt','r')
fwrite = open ('result1.json','w')

for lines in fread:
    fwrite.write(lines)
    
fread.close()

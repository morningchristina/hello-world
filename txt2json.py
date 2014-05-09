#!/usr/bin/env python

import sys

fread = open('11.txt','r')
fwrite = open ('11.json','w')

for lines in fread:
    fwrite.write(lines)
    
fread.close()

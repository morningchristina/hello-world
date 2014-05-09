#!/usr/bin/env python

import sys
fread = open('11.txt','r')
for line in fread:
    line = line.strip()    
    urls = line.split()[0]
    city = line.split()[1]
    print type(urls)    
    

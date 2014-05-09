#!/usr/bin/env python

import sys
import re

f1 = open('/Users/zxwxfczxx/Desktop/soufun_proje_list_all.html','r')
f2 = file('/Users/zxwxfczxx/Desktop/1.json','w')

lines= f1.readlines()

for line in lines:
    reg = "href=\"([\s\S]*?)\">([\s\S]*?)</a></li>"
    imreg = re.compile(reg)
    imglist = re.findall(imreg,line)


    for items in imglist:
        for item in items:
            f2.write(item)
            f2.write('\t\t\t\t\t')
        f2.write('\n')

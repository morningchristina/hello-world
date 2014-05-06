#!/usr/bin/env python
#encoding:utf-8
import re
import sys
fr = open ('/Users/zxwxfczxx/Desktop/view-source.html','r')

fi = file('1.txt','w')

lines = fr.readlines()
for line in lines:
    line = line.decode('utf-8')
    reg ='href="(.+?)" target=.+?>(.+?)</a>'
    imreg = re.compile(reg)
    imglist = re.findall(imreg,line)

    for items in imglist:
        for item in items:
            result = str(item.encode('utf-8'))
            fi.write(result)
            fi.write('\t')
        fi.write('\n')



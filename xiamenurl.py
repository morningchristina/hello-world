#!/usr/bin/env python
#encoding:utf-8
import urllib2
import re
import sys

reload(sys);
sys.setdefaultencoding('utf8')
fr = open('xiamen.txt','r')
fi = file('xiamenresult.txt','a')

lines = fr.readlines()
for line in lines:
    line = line.decode('gbk')
    reg = r"href='(.+)'\s\S>(.+)</a>"
    imreg = re.compile(reg)
    imglist = re.findall(imreg,line)

    for items in imglist:
        for item in items:
            #result = str(item.encode('utf-8'))
            fi.write(item)
            #fi.write('\t')
        fi.write('\n')



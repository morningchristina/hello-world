#!/usr/bin/env python
#-*-coding: gbk-*-

import re
import urllib2
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
fwrite = open('beijing.txt','w')
for i in range(65,91):
    fread = open("/Users/zxwxfczxx/Desktop/soufun/bbs_proj_list_"+chr(i)+".htm")
    lines = fread.readlines()
           
    for line in lines:
        line = line.decode('gbk')
        reg = r"href='(.+)'\s\S>(.+)</a>"
        imreg = re.compile(reg)
        imglist = re.findall(imreg,line)

        for items in imglist:
            for item in items:
                #result = item.encode('gbk')
                fwrite.write(item)
                fwrite.write('\t')
            fwrite.write('\n')


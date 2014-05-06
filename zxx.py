#!/usr/bin/env python
#encoding:utf-8
import re
import sys
fr = open ('/Users/zxwxfczxx/Desktop/soufun_proje_list_all.html','r')

fi = file('/Users/zxwxfczxx/Desktop/1.txt','w')

lines = fr.readlines()    
for line in lines:
    line = line.decode('utf-8')
    reg ="href=\"([\s\S]*?)\">([\s\S]*?)</a></li>"
    imreg = re.compile(reg)
    imglist = re.findall(imreg,line)
    
    for items in imglist:
        for item in items:
            result = str(item.encode('utf-8'))
            fi.write(result)
            fi.write('\t\t\t\t\t')
        fi.write('\n')
       


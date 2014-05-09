#!/usr/bin/env python
#-*-coding: gbk-*-

import re
import urllib2
import sys

reload(sys)
sys.setdefaultencoding('gbk')
fwrite = open('xiamen.txt','a')
for i in range(65,91):
    fread = urllib2.urlopen("http://bbs.xm.soufun.com/bbs_proj_list_"+chr(i)+".htm")
    lines = fread.readlines()
    
    for line in lines:
        line = line.decode('gbk','ignore')
        
        reg = r"href='(.+?)'.+?>(.+?)</a>"
        imreg = re.compile(reg)
        imglist = re.findall(imreg,line)

        for items in imglist:
           for item in items:
               result = item.encode('gbk')
               fwrite.write(result)
               fwrite.write('\t')
               fwrite.write('\n')                             

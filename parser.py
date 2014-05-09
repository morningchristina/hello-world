#!/usr/bin/env python
#-*-coding: utf-8-*-

import urllib2
import sys
import re

fread = open('xiamen.html','r')
fwrite = open('xiamen.txt','w')

lines = fread.readlines()

for line in lines:
	reg = "href=\"([\s\S]*?)\">([\s\S]*?)</a></li>"
	imreg = re.compile(reg)
	imglist = re.findall(imreg,line)
	
	for items in imglist:
		for item in items:
			fwrite.write(item)	
			fwrite.write('\t\t\t\t')
			fwrite.write('\n') 

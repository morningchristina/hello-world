#!/usr/bin/env python
import re

fread = open('/Users/zxwxfczxx/Desktop/redmine/soufun_proje_list_all.html','r')
fwrite = open('1.txt','w')
lines = fread.readlines()
for line in lines:
	reg = "href=\"([\s\S]*?)\">([\s\S]*?)</a></li>"
	urlreg = re.compile(reg)
	urllist = re.findall(urlreg,line)
	for eachurl in urllist:
		for each in eachurl:
			fwrite.write(each)
			fwrite.write('\n')
fread.close()
		
		

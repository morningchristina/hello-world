#!/usr/bin/env python
import sys
import re

fwrite = open('/Users/zxwxfczxx/Desktop/example.txt','w')

def getHtml(url):
    fread= open(url,'r')
    fread.read()
    return fread

def parser():
    reg = r'href=\"([\s\S]*?)\">([\s\S]*?)</a></li>'
    urlreg = re.compile(reg)
    urllist = re.findall(urlreg,fread)

def write(fwrite):
    for eachline in fread:
        eachline.write()


myUrl = getHtml('/Users/zxwxfczxx/Desktop/soufun_proje_list_all.html')
myUrl.parser()
myUrl.write()

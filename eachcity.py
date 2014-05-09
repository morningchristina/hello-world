#!/usr/bin/env python

import sys
import urllib2

fread = open('11.txt','r')
for lines in fread:
    lines = lines.strip()
    url = lines.split()[0]
    city = lines.split()[1]
    fr = urllib2.urlopen(url)
         







#!/usr/bin/env python	
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
word2count = {}
fread = open('result1.txt','r')
fwrite = open('output.txt','w')
count = 1
for lines in fread:
    lines = lines.strip()
    lines = lines.decode('utf-8','ignore')
    uid = lines.split()[0]
    word = lines.split()[1] 
    try:
        count = int(count)
        word2count[word] = word2count.get(word, 0) + count
    except ValueError:
        pass 
for word in word2count:
    fwrite.write(word)
    fwrite.write('\t')
    fwrite.write(str(word2count[word]))
    fwrite.write('\n')
  





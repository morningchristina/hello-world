#/usr/bin/env python
#coding:gbk

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

word2count = {}

fread = open('query-log.txt','r')
fwrite = open('result.txt','w')

for lines in fread:
    lines = lines.strip()
    lines = lines.decode('gbk','ignore') 
    uid = lines.split()[1]
    word = lines.split()[2]
    word2count.setdefault(uid,word) 
    #for item in word2count.items():
     #   item = list(set(item))
       
    for line in word2count:
        line = line.strip()
        word,count = line.split('\t',1)
        try:
            count = int(count)
            word2count[word] = word2count.get(word,0)+count
        except ValueError:
            pass

fread.close()

for word in word2count:
    #fwrite.write(word)
    #fwrite.write('\t')
    #fwrite.write(str(word2count[word]).encode('utf-8'))
    #fwrite.write('\n')
    print word,word2count[word]





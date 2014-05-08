#!/usr/bin/env python
import sys

word2count = {}
for line in sys.stdin:
    line = line.strip()
    word,count = line.split('\t',1)
    try:
        count = int(count)
        word2count[word] = word2count.get(word,0)+count
    except ValueError:
        pass

for word in word2count:
    fwrite.write(word)
    fwrite.write('\t')
    fwrite.write(str(word2count[word]).encode('utf-8'))
    fwrite.write('\n')
    print word,word2count[word]



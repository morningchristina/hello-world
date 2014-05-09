#!/usr/bin/env python

'makeTextFile.py--create text file'

import os

fname = raw_input("please input file name:\n")

while True:
    if os.path.exists(fname):
        print "error:'%s already exists" % fname
    else:
        break

all = []
    
while True:
    entry = raw_input('>')
    if entry =='.':
        break
    else:
        all.append(entry)

fobj = open(fname,'w')
fobj.writelines(['%s%s ' %(x,'\n') for x in all])
fobj.close()
print 'done'

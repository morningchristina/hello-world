#!/usr/bin/env python

'readTextFile.py--read and display text file'

fname = raw_input('enter filename:')
print

try:
    fobj = open(fname,'r')
except IOError,e:
    print "*** file open error:",e
else:
    for eachLine in fobj:
        print eachLine,
    fobj.close()

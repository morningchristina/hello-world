#!/usr/bin/env python

import string

alphas = string.letters + '_'
nums = string.digits
alphnums = alphas +nums
print alphnums

myInput = raw_input("enter a identifier:")
length = len(myInput)

if length > 1:
    if myInput[0] not in alphas:
        print 'invalid'
    else:
        for otherChar in myInput[1:]:
            if otherChar in alphnums:
                print 'ok'
            else:
                print 'invalid'
            break


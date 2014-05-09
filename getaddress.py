#!/usr/bin/env python

import sys
import json

for line in sys.stdin:
    line = line.strip()
    text = json.loads(line)
    address = text[1] 
    fr = open ('http://api.map.baidu.com/geocoder?address=“+address+"&output=json&key=I3PeCzN9abAO4td4z75D03Gp&city=北京','r')
    


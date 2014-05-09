#!/usr/bin/env pthon

import sys
import json

for line in sys.stdin:
    line = line.strip()
    
    content = json.loads(line)
    url = content[0]
    starttext = content[1]
    text = starttext[:-4]

    print '%s\t%s' %(text,url)  


#!/usr/bin/env python
import urllib2,formatter,string
from HTMLParser import HTMLParser  
class MyHTMLParser(HTMLParser):
    def __init__(self): 
        self.links = {}    
        f = formatter.NullFormatter()
        HTMLParser.__init__(self, f)
    def anchor_bgn(self, href, name, type):  
        self.save_bgn() 
        self.link = href
    def anchor_end(self):
        text = string.strip(self.save_end())
        if self.link and text:
             self.links[text] = self.link#self.links.get(text, []) + [self.link]  
page=urllib2.urlopen('file:///Users/zxwxfczxx/Desktop/soufun_proje_list_all.html').read()
parser = MyHTMLParser()
parser.feed(page)
parser.close()

for href, link in linkdemo.links.items():
    print href, "=>", link  
            








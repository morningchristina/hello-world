#!/usr/bin/env python

import urllib2
from HTMLParser import HTMLParser

page=urllib2.urlopen('file:///Users/zxwxfczxx/Desktop/soufun_proje_list_all.html').read()



class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            print  attr
    def handle_data(self, data):
        print  data
    
parser = MyHTMLParser()
parser.feed(page)
parser.close()



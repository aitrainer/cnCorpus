# -*- coding=utf-8 -*-

import sys, getopt
import re
from langconv import *

opts, args = getopt.getopt(sys.argv[1:], "ht:", ["tags="])

tags = []

for op, value in opts:
    if op == "-t" or op == "--tags":
        tags = re.split(r'\|', value)
        #print (tags)
    elif op == "-h":
        #print ("this is help!")
        sys.exit()
    else:
        #print ("op=%s, value=%s" % (op, value))
        sys.exit()

if len(tags) == 0:
    sys.exit()


stops = ['}}']

for line in sys.stdin.readlines():
    for tag in tags:
        rex = re.compile(".*?<" + tag + ">(.*)<\/" + tag + ">.*?")
        reg = rex.match(line.strip())
        if reg:
            text = reg.group(1)
            if len(text) == 0 or text[0] == "|":
                continue
            ms = re.match(r'Wikipedia：(.*)', text)
            if ms:
                text = ms.group(1)
            ms = re.match(r'(.*?)（）(.*)', text)
            while ms:
                text = ms.group(1) + ms.group(2)
                ms = re.match(r'(.*?)（）(.*)', text)
            if len(text) > 1 and text not in stops:
                print (Converter('zh-hans').convert(text))




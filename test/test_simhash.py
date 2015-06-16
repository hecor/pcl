#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, jieba
from pcl.text import Simhash, SimhashIndex, extract_content_from_html

text1 = extract_content_from_html(urllib.urlopen('http://www.leleketang.com/zuowen/122101.shtml').read())
text2 = extract_content_from_html(urllib.urlopen('http://www.leleketang.com/zuowen/148255.shtml').read())

s1 = Simhash(text1)
s2 = Simhash(text2)

print text1
print '%x' % s1.value
print text2
print '%x' % s2.value
print s1.distance(s2)

objs = [(text1, s1)]
index = SimhashIndex(objs, k=3)

print index.bucket_size()
print 'dup count:', len(index.get_near_dups(s2))

index.add(text2, s2)
print 'dup count:', len(index.get_near_dups(s2))


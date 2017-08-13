# coding=utf-8

import re


pattern = re.compile(r"\d+")

m = pattern.match("aaa123bbb456",3,6)

print m.group()

pattern2 = re.compile(r"([a-z]+) ([a-z]+)",re.I)

m = pattern2.match("Hello world hello Python")

print m.group()

pattern3 = re.compile(r"\d+")

m = pattern3.search(r"aaa123bbb456",2,5)

print m.group()

print m.span()

m = pattern3.search(r"aa 1234645 231")

print m.group()


pattern4 = re.compile(r"\d+")

m = pattern4.findall("hello 123456 789")

print m

m = pattern4.finditer("abc123bb456")

for i in m:
    print i.group()

















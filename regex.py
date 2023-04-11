import re

a="We are the Python Programmers, 1) Mrs. P Srujana, 2) Mr. K Gurucharan and 3) Mr. S S Kiran"
b=re.search("S S Kiran",a)#weather S S Kiran is working as Software Developer

print(b)

c=re.findall("S S Kiran",a)#weather S S Kiran is working as Software Developer

print(c)
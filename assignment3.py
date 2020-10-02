#!/usr/bin/python
import re
x = input ("enter number :" )
patt= re.compile('^[1-9][0-9]?$|^100$')
if re.fullmatch(patt,x):
    print('Value is in beetween 0 to 100')
else:
    print('Value is not in beetween 0 to 100')


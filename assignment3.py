#!/usr/bin/python
import re
x = input ("enter number :" )
patt= re.compile('^[1-9][0-9]?$|^100$')
if re.fullmatch(patt,x):
    print('Matched')
else:
    print('Not Matched')


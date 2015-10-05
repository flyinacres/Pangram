__author__ = 'rfischer'
import string

S = raw_input()

p = 1
s =  S.lower()
for x in string.lowercase:
    if not x in s:
        print "not pangram"
        p = 0
        break


if p:
    print "pangram"
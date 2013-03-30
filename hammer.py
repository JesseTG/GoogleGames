'''
goo.gl/72Z69
'''

from math import asin, degrees

g = 9.8

def get_theta(v, d):
    try:
        return degrees(asin((g*d) / (v**2))/2)
    except Exception:
        return "Impossible"

with open('./test.txt') as files:
    files.readline()
    nums = [j.split() for j in files]

answers = [get_theta(int(v), int(d)) for v, d in nums]


for i in range(len(answers)):
    print("Case #%d: %s" % (i + 1, answers[i]))
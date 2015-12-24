#!/usr/bin/python

import sys
import hashlib

filename = sys.argv[1]

badstrings = ["ab", "cd", "pq", "xy"]
vowels = ['a', 'e', 'i', 'o', 'u']

naughty = []
nice = []

for line in open(filename):
  line = line.rstrip()
  vowel_count = 0
  double = False
  badstr = False
  lastch = ''
  # print "Line: ", line

  for c in line:
    if c in vowels:
      vowel_count += 1
    if c == lastch:
      double = True
    lastch = c

  if vowel_count >= 3 and double:
    # Only do this if I have to.
    for bad in badstrings:
      if bad in line:
        badstr = True

  if not badstr and vowel_count >= 3 and double:
    nice.append(line)
  else:
    naughty.append(line)

#print "Naughty count: ", str(len(naughty))
print "Nice count (part1): ", str(len(nice))

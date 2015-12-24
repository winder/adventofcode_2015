#!/usr/bin/python
import sys
import re

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

auntsfile = sys.argv[1]
cluesfile = sys.argv[2]

aunts = dict()
clues = dict()

for line in open(auntsfile):
  m = re.search("Sue (\d+): (.*)", line)
  v = re.findall("(\w+): (\d+),?", m.group(2))
  aunts[m.group(1)] = dict()
  for pair in v:
    aunts[m.group(1)][pair[0]] = int(pair[1])

for line in open(cluesfile):
  c,v = re.search("(\w+): (\d+)", line).groups()
  clues[c] = int(v)

# Sum of first N numbers
total1 = (len(aunts)*(len(aunts)+1))/2
total2 = total1

def compareClues(key, clueVal, auntVal, part1):
  if part1:
    return clueVal != auntVal
  else:
    if key in ["cats","trees"]:
      return auntVal <= clueVal
    if key in ["pomeranians", "goldfish"]:
      return auntVal >= clueVal
    else:
      return auntVal != clueVal

excluded1 = set()
excluded2 = set()
for c in clues.keys():
  for a in aunts.keys():
    if c in aunts[a] and compareClues(c, clues[c], aunts[a][c], True):
      if not a in excluded1:
        total1 -= int(a)
        excluded1.add(a)
    if c in aunts[a] and compareClues(c, clues[c], aunts[a][c], False):
      if not a in excluded2:
        total2 -= int(a)
        excluded2.add(a)

print "Gifter (Part 1): ", total1
print "Gifter (Part 2): ", total2

#!/usr/bin/python
import sys
import re
import itertools

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

filename = sys.argv[1]
people = set()
preferences = dict()

for line in open(filename):
  p1,s,h,p2 = re.search("(.*) would (.*) (.*) happiness units by sitting next to (.*).", line).groups()
  people.add(p1)
  if s == "lose":
    h = -1 * int(h)
  preferences[p1 + ' ' + p2] = int(h)

#print people
#print preferences

def calcHapiness(arrangement):
  ppl = len(arrangement)
  hap = 0
  # Remove the -1 for part 1
  for i in range(ppl - me):
    hap += preferences[arrangement[i] + ' ' + arrangement[(i+1)%ppl]]
    hap += preferences[arrangement[(i+1)%ppl] + ' ' + arrangement[i]]
  return hap

def getMax():
  maximum = False
  for perm in itertools.permutations(people):
    val = calcHapiness(perm)
    if not maximum:
      maximum = val
    elif maximum < val:
      maximum = val
  return maximum

me = 0
print "Part 1: ", getMax()
me = 1
print "Part 2: ", getMax()

#!/usr/bin/python
import sys
import itertools

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

containers = map(int, open(sys.argv[1]).read().split())
goalsize = int(sys.argv[2])

combinations = 0
combinationsMinContainers = False
for i in range(1,len(containers)+1):
  for perm in itertools.combinations(containers, i):
    if sum(perm) == goalsize:
      combinations += 1
  if combinations > 0 and not combinationsMinContainers:
    combinationsMinContainers = combinations

print "Combinations:", combinations
print "Combinations for minimum num:", combinationsMinContainers

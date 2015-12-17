#!/usr/bin/python
import sys
import itertools

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

containers = open(sys.argv[1]).read().split()
goalsize = int(sys.argv[2])

combinations = 0
combinationsMinContainers = False
for i in range(1,len(containers)+1):
  for perm in itertools.combinations(containers, i):
    s = reduce(lambda x,y: int(x)+int(y), perm)
    if s == goalsize:
      #print perm,"=",s
      combinations += 1
  if combinations > 0 and not combinationsMinContainers:
    combinationsMinContainers = combinations

print "Combinations:", combinations
print "Combinations for minimum num:", combinationsMinContainers

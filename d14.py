#!/usr/bin/python
import sys
import re
import itertools

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

filename = sys.argv[1]
duration = int(sys.argv[2])
speeds = dict()

for line in open(filename):
  d,s,d1,d2 = re.search("(.*) can fly (.*) km/s for (.*) seconds, but then must rest for (.*) seconds.", line).groups()
  speeds[d] = list((s, d1, d2, "-", 0))

def getWinners(i):
  i = int(i)
  val = 0
  winner = False
  for d in speeds:
    if not winner:
      winner = list()
      winner.append(d)
    if val == speeds[d][i]:
      winner.append(d)
    elif val < speeds[d][i]:
      val = speeds[d][i]
      winner = list()
      winner.append(d)
  return winner

def calcDistance(s, d1, d2, t):
  fullloops = t/(d1+d2)
  remainder = min(t%(d1+d2), d1)
  return s * fullloops * d1 + remainder * s

for i in range(duration):
  for d in speeds:
    ob = speeds[d]
    ob[3] = calcDistance(int(ob[0]),int(ob[1]),int(ob[2]),i+1)
  front = getWinners(3)
  for d in front:
    speeds[d][4] = int(speeds[d][4]) + 1

# By distance
winner = getWinners(3)[0]
print "Winner (dist):",winner,speeds[winner]
print "\tPart 1:", speeds[winner][3]

# By points
winner = getWinners(4)[0]
print "Winner (points):",winner,speeds[winner]
print "\tPart 2:", speeds[winner][4]

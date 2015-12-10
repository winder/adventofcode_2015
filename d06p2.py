#!/usr/bin/python

import sys
import re

filename = sys.argv[1]

''' initialize 2D array of brightnesses to 0 '''
grid = [[0]*1000 for i in range(1000)]

for line in open(filename):
  line = line.rstrip()
  m = re.search('(?:turn )?(off|on|toggle)+ (\d+),(\d+) through (\d+),(\d+)', line)
  fromx=int(m.group(2))
  tox=int(m.group(4))
  fromy=int(m.group(3))
  toy=int(m.group(5))

  for x in range(fromx, tox+1):
    for y in range(fromy, toy+1):
      if m.group(1) == 'toggle':
        grid[x][y] = grid[x][y] + 2
      elif m.group(1) == 'on':
        grid[x][y] += 1
      else:
        grid[x][y] -= 1
      if grid[x][y] < 0:
        grid[x][y] = 0

answer = 0
for x in range(1000):
  for y in range(1000):
    answer+=grid[x][y]
print "Light power: ", str(answer)

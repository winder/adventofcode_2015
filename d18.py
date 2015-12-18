#!/usr/bin/python
import sys
import itertools
import numpy
filename = sys.argv[1]
steps = int(sys.argv[2])

stuckCorners = False

with open(filename, 'r') as f:
  length = len(f.readline().rstrip())
  x_bound = length
  y_bound = length

lights=numpy.zeros(shape=(x_bound,y_bound))

y = 0
for line in open(filename):
  x = 0
  for c in line.rstrip():
    if c == '#':
      lights[y][x] = 1
    x += 1
  y += 1

# print lights

def updateLight(matrix, x, y):
  litNeighbors=0

  lookRight = (x+1) < x_bound
  lookLeft = (x-1) >= 0
  lookUp = (y-1) >= 0
  lookDown = (y+1) < y_bound

  if stuckCorners and ((not lookRight and not lookUp) or (not lookRight and not lookDown) or (not lookLeft and not lookUp) or (not lookLeft and not lookDown)):
    return 1

  if lookRight and matrix[y][x+1] == 1:
    litNeighbors += 1
  if lookLeft and matrix[y][x-1] == 1:
    litNeighbors += 1
  if lookDown and matrix[y+1][x] == 1:
    litNeighbors += 1
  if lookUp and matrix[y-1][x] == 1:
    litNeighbors += 1
  if lookRight and lookUp and matrix[y-1][x+1]:
    litNeighbors += 1
  if lookRight and lookDown and matrix[y+1][x+1]:
    litNeighbors += 1
  if lookLeft and lookUp and matrix[y-1][x-1]:
    litNeighbors += 1
  if lookLeft and lookDown and matrix[y+1][x-1]:
    litNeighbors += 1

  if matrix[y][x] == 1 and (litNeighbors < 2 or litNeighbors > 3):
    return 0

  if matrix[y][x] == 0 and litNeighbors == 3:
    return 1

  return matrix[y][x]

def update(matrix):
  scratch=numpy.zeros(shape=(x_bound,y_bound))
  for x in range(x_bound):
    for y in range(y_bound):
      scratch[y][x] = updateLight(matrix, x, y)
  return scratch
  
initialLights = lights.copy()

for i in range(steps):
  lights = update(lights)
print "Part1:", numpy.sum(lights)

lights = initialLights
stuckCorners = True
for i in range(steps):
  lights = update(lights)
print "Part2:", numpy.sum(lights)

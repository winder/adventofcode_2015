#!/usr/bin/python
import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

filename = sys.argv[1]
houses = dict()

coord = [0,0]
rcoord = [0,0]
santa = True

''' Mark the starting location '''
houses["x0y0"] = 1

def update_dir(char, coord):
  if c == ">":
    coord[0] = coord[0] + 1
  elif c == "<":
    coord[0] = coord[0] - 1
  elif c == "^":
    coord[1] = coord[1]+ 1
  elif c == "v":
    coord[1] = coord[1]- 1

with open(filename) as f:
  while True:
    c = f.read(1)
    if not c:
      print "End of file"
      break

    ''' update coordinate '''
    if santa:
      update_dir(c, coord)
      cur = coord
    else:
      update_dir(c, rcoord)
      cur = rcoord

    ''' comment out for part 1 '''
    santa = not santa

    ''' save location '''
    location = 'x' + str(cur[0]) + 'y' + str(cur[1])
    houses[location] = 1
    '''print "Read a character:", c'''

print "Houses visited: ", len(houses)

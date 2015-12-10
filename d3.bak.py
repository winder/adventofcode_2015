#!/usr/bin/python

import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

filename = sys.argv[1]
houses = dict()

xcoord = 0
ycoord = 0
rxcoord = 0
rycoord = 0
santa = True

curxcoord = 0;
curycoord = 0;

houses["x0y0"] = 1

with open(filename) as f:
  while True:
    c = f.read(1)

    ''' update coordinate '''
    if santa:
      if c == ">":
        xcoord = xcoord + 1
      elif c == "<":
        xcoord = xcoord - 1
      elif c == "^":
        ycoord = ycoord + 1
      elif c == "v":
        ycoord = ycoord - 1
      curxcoord = xcoord
      curycoord = ycoord
    else:
      if c == ">":
        rxcoord = rxcoord + 1
      elif c == "<":
        rxcoord = rxcoord - 1
      elif c == "^":
        rycoord = rycoord + 1
      elif c == "v":
        rycoord = rycoord - 1
      curxcoord = rxcoord
      curycoord = rycoord

    ''' comment out for part 1 '''
    santa = not santa

    ''' save location '''
    location = 'x' + str(curxcoord) + 'y' + str(curycoord)

    if location in houses:
      houses[location] = 1
    else:
      houses[location] = int(houses.get(location) or 1) + 1

    print "Location: " + str(location) + ", presents: " + str(houses.get(location))


    if not c:
      print "End of file"
      break
    print "Read a character:", c

print "Houses visited: ", len(houses)

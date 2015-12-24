#!/usr/bin/python
import sys

filename = sys.argv[1]
houses = dict()

coord = [0,0]
scoord = [0,0]
ecoord = [0,0]
santa = True

# Mark the starting location
houses["x0y0"] = [1,1,1]

def update_dir(char, coord):
  if c == ">":
    coord[0] = coord[0] + 1
  elif c == "<":
    coord[0] = coord[0] - 1
  elif c == "^":
    coord[1] = coord[1]+ 1
  elif c == "v":
    coord[1] = coord[1]- 1

def updateHouse(arr, idx, idxidx):
  if not idx in arr:
    arr[idx] = [0,0,0]
  arr[idx][idxidx] = 1

with open(filename) as f:
  while True:
    c = f.read(1)
    if not c:
      break

    # Part 1
    #update coordinate
    update_dir(c, coord)
    # save location
    location = 'x' + str(coord[0]) + 'y' + str(coord[1])
    updateHouse(houses, location, 0)

    # Part 2
    #update coordinate
    if santa:
      update_dir(c, scoord)
      cur = scoord
    else:
      update_dir(c, ecoord)
      cur = ecoord

    # save location
    location = 'x' + str(cur[0]) + 'y' + str(cur[1])
    if santa:
      updateHouse(houses, location, 1)
    else:
      updateHouse(houses, location, 2)
    santa = not santa

def sumIdx(h, part1):
  total = 0
  for house in h.values():
    if part1:
      total += int(house[0])
    else:
      total += max(int(house[1]),int(house[2]))
  return total

part1 = sumIdx(houses,True)
part2 = sumIdx(houses,False)
print "Houses visited (part1): ", part1
print "Houses visited (part2): ", part2

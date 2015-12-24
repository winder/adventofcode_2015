#!/usr/bin/python
import sys

filename = sys.argv[1]
locations = set()
routes = dict()


for line in open(filename):
  town1, _, town2, _, cost = line.rstrip().split()
  locations.add(town1)
  locations.add(town2)
  if not town1 in routes:
    routes[town1] = dict()
  if not town2 in routes:
    routes[town2] = dict()
  routes[town1][town2] = cost
  routes[town2][town1] = cost

def compare(left, right):
  if operator == '>':
    return left > right
  elif operator == '<':
    return left < right
  print "Invalid operator '" + operator + "'"
  sys.exit(1)

def visit(cost, visited, location):
  visited.append(location)

  if len(visited) == len(locations):
    return cost

  price = -1
  for dest in locations:
    if dest not in visited:
      if dest in routes[location]:
        tmp = visit(cost+int(routes[location][dest]), list(visited), dest)
        if price == -1 or compare(tmp, price):
          price = tmp
  return price

operator = '<'
visited = []
price = -1
for town in locations:
  cost = visit(0, list(visited), town)
  if price == -1 or compare(cost, price):
    price = cost

print "Result (part1):", price

operator = '>'
visited = []
price = -1
for town in locations:
  cost = visit(0, list(visited), town)
  if price == -1 or compare(cost, price):
    price = cost
print "Result (part2):", price

#!/usr/bin/python
import sys
import json
import collections

filename = sys.argv[1]

json_object = json.load(open(filename))
total=0

def part_two(d):
  for key in d:
    if d[key] == "red":
      return True
  return False

def is_digit(n):
  try:
    int(n)
    return True
  except ValueError:
    return False

def thing(l):
  if is_digit(l):
    #print l
    global total
    total = total + int(l)

def recurse(nextOb):
  if not isinstance(nextOb, (list,dict,tuple)):
    thing (nextOb)
  else:
    if isinstance(nextOb, dict):
      if part_two(nextOb):
        return
      for key in nextOb:
        thing(key)
        recurse(nextOb[key])
    elif isinstance(nextOb,(list,tuple)):
      for key in nextOb:
        recurse(key)


for key in json_object:
    recurse(json_object[key])

print "Total:", total

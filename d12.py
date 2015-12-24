#!/usr/bin/python
import sys

filename = sys.argv[1]

with open(filename) as f:
  negate = 1
  nums = list()
  total = 0
  curNum = 0
  while True:
    c = f.read(1)
    if c == '-':
      negate = -1
    if c == '-' or c.isdigit():
      if c.isdigit():
        curNum *= 10
        curNum += int(c)
    else:
      if curNum != 0:
        nums.append(curNum * negate)
        total += (curNum * negate)
        #print "Adding to total:", (curNum * negate)
        curNum = 0
      negate = 1

    if not c:
      #print "End of file"
      break

print "Sum:", total

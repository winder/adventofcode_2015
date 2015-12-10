#!/usr/bin/python
import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

value = open(sys.argv[1]).readline().rstrip()
iterations = int(sys.argv[2])

for i in range(iterations):
  nextval = ""
  char = '*'
  count = 0
  for c in value:
    if c != char:
      if count != 0:
        nextval += str(count)
        nextval += char
      count = 1
      char = c
    else:
      char = c
      count += 1
  nextval += str(count)
  nextval += char
  ''' print value, "->", nextval '''
  value = nextval

print "Length after",iterations,"iterations:",len(nextval)

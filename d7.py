#!/usr/bin/python
import sys
import re

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

filename = sys.argv[1]
solvefor = sys.argv[2]
patterns = dict()

def is_digit(n):
  try:
    int(n)
    return True
  except ValueError:
    return False

def operate(left, op, right):
  left = int(left)
  right = int(right)

  '''
  print "\nCalculating: ", str(left), " ", op, " ", str(right), "\n"
  '''
  if op == 'NOT':
    return ~right
  elif op == 'AND':
    return left & right
  elif op == 'OR':
    return left | right
  elif op == 'RSHIFT':
    return left >> right
  elif op == 'LSHIFT':
    return left << right
  else:
    return right

def solve_loop(key):
  return


def solve(key):
  '''
  print "FOR KEY: ", key, " patt: ", patterns[key]
  '''
  left = patterns[key][0]
  op = patterns[key][1]
  right = patterns[key][2]

  if not is_digit(left):
    left = solve(left)
    patterns[key][0] = left
  if not is_digit(right):
    right = solve(right)
    patterns[key][2] = right

  return operate(left, op, right)


''' Build a dictionary to reduce '''
for line in  open(filename):
  line = line.rstrip()
  '''
  print "Line: ", line, "\n"
  print "Idx space: ", str(line.index(" ")), ", ", line[line.index(" ")+1]
  '''

  if line[line.index(" ")+1] == "-" and line[line.index(" ")+2] == ">":
    m = re.search('(.*) -> (.*)', line)
    patterns[m.group(2)]=[0, "NONE", m.group(1)]
  elif line.startswith("NOT"):
    m = re.search('(.*) (.*) -> (.*)', line)
    patterns[m.group(3)]=[0, m.group(1), m.group(2)]
  else:
    m = re.search('(.*) (.*) (.*) -> (.*)', line)
    patterns[m.group(4)]=[m.group(1), m.group(2), m.group(3)]

''' Solve for 'a' '''
print "Solving for ", solvefor, ": ", str(solve(solvefor))

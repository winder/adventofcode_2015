#!/usr/bin/python
import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

filename = sys.argv[1]
def linesize2(line):
  size = len(line) 
  escaping = False
  hexStop = 0

  for c in line:
    if escaping:
      if c == 'x':
        size -= 1
        hexStop = 2
      elif hexStop > 0:
        hexStop -= 1
      if hexStop == 0:
        escaping = False
    elif c == '"':
      size += 2
      continue
    elif c == '\\':
      size += 2
      escaping = True
  return size

def linesize(line):
  size = len(line)
  escaping = False
  hexStop = 0

  for c in line:
    if escaping:
      if c == 'x':
        size -= 2
        hexStop = 2
      elif hexStop > 0:
        hexStop -= 1
      if hexStop == 0:
        escaping = False
    elif c == '"':
      size -= 1
      continue
    elif c == '\\':
      size -= 1
      escaping = True
  return size

escaped = 0
memsize = 0
literal = 0
for line in open(filename):
  line = line.rstrip()
  literal += len(line)
  size = linesize(line)
  memsize += size
  size2 = linesize2(line)
  escaped += size2
  '''
  print "Size of " + line + ": ", len(line), "Memsize:",size, "Escaped:", escaped
  '''

print "Total len:", literal, "Memory size:", memsize, "Escaped size:", escaped
print "Answer 1:", literal-memsize
print "Answer 2:", escaped - literal

#!/usr/bin/python
import sys

filename = sys.argv[1]

naughty = []
naughty_cnt=0
nice = []
nice_cnt=0

for line in open(filename):
  line = line.rstrip()
  pair = False
  sep = False

  i = 0
  while (not pair or not sep) and i < (len(line)-1):
    if not sep:
      if i+2 < len(line):
        if line[i] == line[i+2]:
          sep = True
          sepp = line[i:i+3]

    if not pair:
      sub = line[i:i+2]
      if sub in line[i+2:]:
        pair = True
      else:
        sub = ""
    i+=1

  if not sep:
    sepp = ""

  if pair and sep:
    nice.append(line)
    nice_cnt+=1
  else:
    naughty.append(line)
    naughty_cnt+=1

  #print "Line: ", line, "\tpairs: ", sepp, "\tsep: ", sub

#print "Naughty count: ", str(len(naughty))
print "Nice count (part2): ", str(len(nice))

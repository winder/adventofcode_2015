#!/usr/bin/python
import sys
import re

filename = sys.argv[1]
registerNames = ('a', 'b')


instructionInputs = list()
for line in open(filename):
  instructionInputs.append(re.split(', | ',line.rstrip()))

#for inst in instructions:
#  print inst

def getValue(val):
  ret = int(val[1:])
  if val[0] == '+':
    return ret
  if val[0] == '-':
    return ret * -1

def process(index, registers, instructions):
  rule = instructions[index]

  if rule[0] == "hlf":
    registers[rule[1]] /= 2
    return index + 1
  elif rule[0] == "tpl":
    registers[rule[1]] *= 3
    return index + 1
  elif rule[0] == "inc":
    registers[rule[1]] += 1
    return index + 1
  elif rule[0] == "jmp":
    return index + getValue(rule[1])
  elif rule[0] == "jie":
    if registers[rule[1]] % 2 == 0:
      return index + getValue(rule[2])
    return index + 1
  elif rule[0] == "jio":
    if registers[rule[1]] == 1:
      return index + getValue(rule[2])
    return index + 1

myRegisters = dict()
for r in registerNames:
  myRegisters[r] = 0
idx=0
while idx < len(instructionInputs):
  #print idx, myRegisters
  idx = process(idx, myRegisters, instructionInputs)

print "Part 1:", idx, myRegisters

for r in registerNames:
  myRegisters[r] = 0
myRegisters['a'] = 1
idx=0
while idx < len(instructionInputs):
  #print idx, myRegisters
  idx = process(idx, myRegisters, instructionInputs)

print "Part 2:", idx, myRegisters

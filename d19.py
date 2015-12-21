#!/usr/bin/python
import sys
import re

filename = sys.argv[1]
expansions = dict()
expansionKeys = set()
reductions = dict()
reductionKeys = set()
initialElements = list()
target = ''

# Build up substitution expansions and reductions
for line in  open(filename):
  line = line.rstrip()
  m = re.search('(\w+) => (\w+)', line)
  if m:
    if m.group(1) == 'e':
      initialElements.append(m.group(2))
      continue
    expansionKeys.add(m.group(1))
    reductionKeys.add(m.group(2))
    if not m.group(1) in expansions:
      expansions[m.group(1)] = list()
    expansions[m.group(1)].append(m.group(2))
    if not m.group(2) in reductions:
      reductions[m.group(2)] = list()
    reductions[m.group(2)].append(m.group(1))
  elif line != '':
    target = line
    break

# Search for all unique substitutions from a current state
def nextSteps(initial):
  results = set()
  for token in expansionKeys:
    for m in re.finditer(token, initial):
      for sub in expansions[token]:
        results.add(initial[:m.start()] + sub + initial[m.end():])
  return results

# Generator wrapper for nextSteps function
def nextStepGenerator(initial):
  results = list(nextSteps(initial))
  for s in results:
    yield s

print "Part 1:", len(nextSteps(target))

# Idea 1
# Breadth first search wont work, the tree is too wide.

# Idea 2
# Build up from initial expansions also taking a verylong time
# This was my initial solution. I'm not sure if it would finish!

'''
def targetGenerator(depth, startingMolecule, goal, goalLength):
  # Early exit condition
  if len(startingMolecule) >  goalLength:
    return

  # Goal condition
  if startingMolecule == goal:
    yield depth

  # Tail recursion
  for nex in nextStepGenerator(startingMolecule):
    for steps in targetGenerator(depth + 1, nex, goal, goalLength):
      yield steps

minimum = False
for start in expansions['e']:
  for steps in targetGenerator(0, start, target, len(target)):
    if not minimum or steps < minimum:
      print "Possible:", steps
      minimum = steps
'''

# Suggestion from reddit...
# ================================================ #
# Instead of building up from the initial element, #
# reduce down from the starting element.           #
# ================================================ #

# Search for all unique substitutions from a current state
def previousSteps(initial):
  results = set()
  for token in reductionKeys:
    for m in re.finditer(token, initial):
      for sub in reductions[token]:
        results.add(initial[:m.start()] + sub + initial[m.end():])
  return results

# Generator wrapper for nextSteps function
def previousStepGenerator(initial):
  results = list(previousSteps(initial))
  results.sort(key = lambda s: len(s))
  for s in results:
    yield s

def sourceGenerator(depth, startingMolecule, goals):
  if startingMolecule in goals:
    yield depth
  for nex in previousStepGenerator(startingMolecule):
    for y in sourceGenerator(depth + 1, nex, goals):
      yield y

for d in sourceGenerator(1, target, initialElements):
  print "Part 2:", d
  sys.exit(0)

#!/usr/bin/python
import sys
import operator
import itertools

presents = map(int, open(sys.argv[1]).read().split())

def findMinEntanglementThree():
  group_weight = sum(presents)/3
  numCombos = 0
  minEntanglement = False
  for size1 in range(1,len(presents)):
    for g1 in itertools.combinations(presents, size1):
      if not sum(g1) == group_weight:
        continue
      remain1 = list(set(presents) - set(g1))
      for size2 in range(len(presents)-size1):
        for g2 in itertools.combinations(remain1, size2):
          if not sum(g2) == group_weight:
            continue
          g3 = list(set(remain1) - set(g2))
          if sum(g1) == sum(g2) == sum(g3):
            numCombos += 1
            entanglement = reduce(operator.mul, g1, 1)
            if not minEntanglement or entanglement < minEntanglement:
              minEntanglement = entanglement
      if numCombos > 0:
        return minEntanglement

def findMinEntanglementFour():
  group_weight = sum(presents)/4
  numCombos = 0
  minEntanglement = False
  for size1 in range(1,len(presents)):
    for g1 in itertools.combinations(presents, size1):
      if not sum(g1) == group_weight:
        continue
      remain1 = list(set(presents) - set(g1))

      for size2 in range(len(presents)-size1):
        for g2 in itertools.combinations(remain1, size2):
          if not sum(g2) == group_weight:
            continue
          remain2 = list(set(remain1) - set(g2))

          for size3 in range(len(presents)-size1-size2):
            for g3 in itertools.combinations(remain2, size3):
              if not sum(g3) == group_weight:
                continue

            g4 = list(set(remain2) - set(g3))
            if sum(g1) == sum(g2) == sum(g3) == sum(g4):
              numCombos += 1
              entanglement = reduce(operator.mul, g1, 1)
              if not minEntanglement or entanglement < minEntanglement:
                minEntanglement = entanglement
      if numCombos > 0:
        return minEntanglement

print "Part 1:", findMinEntanglementThree()
print "Part 2:", findMinEntanglementFour()

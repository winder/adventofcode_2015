#!/usr/bin/python
import sys
import copy

#spells[name] = (mana_cost, damage, heal, armor, mana, duration)
# 0 duration means the spell is instant
spells = dict()
spells['Magic Missile'] = (53 , 4,  0, 0, 0  ,  0)
spells['Drain']         = (73 , 2,  2, 0, 0  ,  0)
spells['Shield']        = (113, 0,  0, 7, 0  ,  6)
spells['Poison']        = (173, 3,  0, 0, 0  ,  6)
spells['Recharge']      = (229, 0,  0, 0, 101,  5)

castOrder = list()
castOrder.append('Magic Missile')
castOrder.append('Drain')
castOrder.append('Shield')
castOrder.append('Poison')
castOrder.append('Recharge')

activeEffects = dict()

# Simulate a fight, return the winner
pHp = 0
pMp = 1
bHp = 2
bD = 3
eE = 4
mC = 5
depth = 6
spellOrder = 7
#def simulationGenerator(pHp, pMp, bHp, bD, effects, manaCost):
def simulationGenerator(state):

  if globalMinimum and state[pMp] > globalMinimum:
    return

  #print "Mana:", state[pMp]
  #print pHp, pMp, bHp, bD, effects, manaCost
  pAc = 0

  # Apply effects at start of player turn
  for e in state[eE].keys():
    state[bHp] -= spells[e][1]
    state[pHp] += spells[e][2]
    pAc += spells[e][3]
    state[pMp] += spells[e][4]
    state[eE][e] -= 1
    if state[eE][e] == 0:
      del state[eE][e]

  # Hard mode
  if globalHard:
    state[pHp] -= 1
  if state[pHp] <= 0:
    return

  if state[bHp] <= 0:
    yield "Player", state[mC], state
    return

  # Simulate all combinations of spells
  for s in castOrder:
    if s not in state[eE] and spells[s][0] <= state[pMp]:
      #print "Casting", s
      nextState = copy.deepcopy(state)
      #nextState[spellOrder].append(s)
      nextState[depth] += 1
      if depth > globalMaxDepth:
        return
      nextState[mC] += spells[s][0]
      nextState[pMp] -= spells[s][0]

      # Instant spell
      if spells[s][5] == 0:
        nextState[bHp] -= spells[s][1]
        nextState[pHp] += spells[s][2]
      else:
        nextState[eE][s] = spells[s][5]

      # Did boss die after my turn?
      if nextState[bHp] <= 0:
        yield "Player", nextState[mC], nextState
        continue

      pAc = 0
      # Apply effects at start of boss turn
      for e in nextState[eE].keys():
        nextState[bHp]   -= spells[e][1]
        nextState[pHp]   += spells[e][2]
        pAc              += spells[e][3]
        nextState[pMp]   += spells[e][4]
        nextState[eE][e] -= 1
        if nextState[eE][e] == 0:
          del nextState[eE][e]

      # Did boss die before his turn?
      if nextState[bHp] <= 0:
        yield "Player", nextState[mC], nextState
        continue

      nextState[pHp] -= max(1, nextState[bD] - pAc)
      if nextState[pHp] <= 0:
        continue

      for r,y,s in simulationGenerator(nextState):
        yield r,y,s

globalMaxDepth = 13
globalHard = False
globalMinimum= False
state = [50, 500, 71, 10, dict(), 0, 0, list()]
#state = [50, 500, 51, 9, dict(), 0, 0, list()]
for r,y,s in simulationGenerator(state):
  if r == "Player":
    if not globalMinimum or y < globalMinimum:
      globalMinimum = y
print "Part 1 (easy):", globalMinimum

globalHard = True
globalMinimum= False
state = [50, 500, 71, 10, dict(), 0, 0, list()]
#state = [50, 500, 51, 9, dict(), 0, 0, list()]
for r,y,s in simulationGenerator(state):
  if r == "Player":
    if not globalMinimum or y < globalMinimum:
      globalMinimum = y
print "Part 2 (hard):", globalMinimum

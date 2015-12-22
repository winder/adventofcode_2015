#!/usr/bin/python
import sys
import re
import itertools
import operator

bossfile = sys.argv[1]
itemsfile = sys.argv[2]

boss = dict()
for line in open(bossfile):
  val = line.split()
  if val[0] == "Hit":
    boss["Hit Points"] = int(val[2])
  elif val[0] == "Damage:":
    boss["Damage"] = int(val[1])
  if val[0] == "Armor:":
    boss["Armor"] = int(val[1])

items = dict()
for line in open(itemsfile):
  m = re.search('(\w+):.*Cost.*Damage.*Armor', line)
  if m:
    cat = m.group(1)
    items[m.group(1)] = list()
    continue
  m = re.search('(.*)\s+(\d+)\s+(\d+)\s+(\d+)', line)
  if m:
    i=(int(m.group(2)), int(m.group(3)), int(m.group(4)), m.group(1).rstrip())
    items[cat].append(i)

'''
print boss
for cat in items.keys():
  print "\nCategory:", cat
  for item in items[cat].keys():
    print item,items[cat][item]
'''

# Generate player stats combinations (DAMAGE, ARMOR, HP, TOTAL_COST)
# 1 Weapon
# 0-1 Armor
# 0-2 Rings

playerCombinations = set()

# Armor configurations

weaponConfigurations = list()
for i in items['Weapons']:
  weaponConfigurations.append(i)

armorConfigurations = list()
for i in items['Armor']:
  armorConfigurations.append(i)
armorConfigurations.append((0,0,0,'None'))

ringConfigurations = list()
for i in items['Rings']:
  ringConfigurations.append(i)
for i in itertools.combinations(items['Rings'], 2):
  ringConfigurations.append(map(operator.add, i[0], i[1]))
ringConfigurations.append((0,0,0,'None'))

'''
print "Weapon configs:"
print weaponConfigurations
print "Armor configs:"
print armorConfigurations
print "Ring configs:"
print ringConfigurations
'''

combinations = list()
for a in weaponConfigurations:
  for b in armorConfigurations:
    for c in ringConfigurations:
      combinations.append(map(operator.add, map(operator.add, a, b), c))

# Simulate a fight, return the winner
def simulate(boss, player):
  bHp = boss[2]
  pHp = player[2]
  while True:
    bHp -= max((player[0] - boss[1]), 1)
    if bHp <= 0:
      return player
    pHp -= max((boss[0] - player[1]), 1)
    if pHp <= 0:
      return boss


boss = (boss["Damage"], boss["Armor"], boss["Hit Points"], 'Boss')

# Part 1, cheapest win
equipmentCombination = False
for equipment in combinations:
  player =  (equipment[1], equipment[2], 100)
  winner = simulate(boss, player)
  if winner == player:
    if not equipmentCombination or (equipment[0] < equipmentCombination[0]):
      equipmentCombination = equipment

print "Part 1 (Cheapest win):\n\tequipment:",equipmentCombination,"\n\tcost:",equipmentCombination[0]

# Part 2, expensive defeat
equipmentCombination = False
for equipment in combinations:
  player =  (equipment[1], equipment[2], 100)
  winner = simulate(boss, player)
  if winner == boss:
    if not equipmentCombination or (equipment[0] > equipmentCombination[0]):
      equipmentCombination = equipment

print "Part 2 (Expensive loss):\n\tequipment:",equipmentCombination,"\n\tcost:",equipmentCombination[0]

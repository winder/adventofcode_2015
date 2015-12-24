#!/usr/bin/python
import sys
import re

filename = sys.argv[1]
scoops = int(sys.argv[2])
maxCal = -1

if len(sys.argv) == 4:
  maxCal = int(sys.argv[3])

ingredients = dict()

for line in open(filename):
  i, cap, d, f, t, cal = re.search("(.*): capacity (.*), durability (.*), flavor (.*), texture (.*), calories (.*)", line).groups()
  ingredients[i] = [cap, d, f, t, cal]

for i in ingredients.keys():
  print i, "\t", ingredients[i]

def calcScore(recipe, ingredients, maxCal):
  prop = [0] * 4
  cal = 0
  # for each property
  for i in ingredients:
    cal += int(recipe[i]) * int(ingredients[i][4])
    for p in range(4):
    # add each ingredients value for property
      prop[p] += int(recipe[i]) * int(ingredients[i][p])

  for i in range(4):
    if (prop[i] <0):
      prop[i] = 0

  if maxCal > 0 and cal > maxCal:
    return 0,0

  #print prop
  return reduce(lambda x,y: x*y, prop), cal
  
# Initialize each ingredient to get over the initial hump
recipe = dict()
for i in ingredients:
  recipe[i] = 5

def sz(r):
  tot = 0
  for i in r.keys():
    tot += r[i]
  return tot

# Add in one ingredient at a time
while sz(recipe) < scoops:
  bestNextValue = -1
  bestNextIdx = -1
  # Find the best next scoop
  for i in ingredients:
    recipe[i] += 1
    frac = float(sz(recipe)) / scoops
    val, cal = calcScore(recipe, ingredients, frac*maxCal)
    if val > bestNextValue:
      bestNextValue = val
      bestNextIdx = i
    recipe[i] -= 1
  # Add best next scoop
  recipe[bestNextIdx] += 1

s,c = calcScore(recipe, ingredients, maxCal)
print recipe, "Score:", s, "Calories:",c

# For part 2, got an answer that might be close
# manually tweak the result...? Didn't work
"""
recipe['Frosting']      = 26
recipe['Butterscotch']  = 27
recipe['Candy']         = 23
recipe['Sugar']         = 24

s,c = calcScore(recipe, ingredients, maxCal)
print recipe, "Score:", s, "Calories:",c
"""

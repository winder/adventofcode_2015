#!/usr/bin/python
import sys
import re

filename = sys.argv[1]
scoops = int(sys.argv[2])
calAmt = -1

if len(sys.argv) == 4:
  calAmt = int(sys.argv[3])

ingredients = dict()

for line in open(filename):
  i, cap, d, f, t, cal = re.search("(.*): capacity (.*), durability (.*), flavor (.*), texture (.*), calories (.*)", line).groups()
  ingredients[i] = [cap, d, f, t, cal]

def calcScore(recipe, ingredients, calAmt):
  prop = [0] * 4
  cal = 0
  # for each property
  for i in ingredients:
    cal += int(recipe[i]) * int(ingredients[i][4])
    # add each ingredients value for property
    for p in range(4):
      prop[p] += int(recipe[i]) * int(ingredients[i][p])

  for i in range(4):
    if (prop[i] <0):
      prop[i] = 0

  if calAmt > 0 and cal != calAmt:
    return 0,0

  #print prop
  return reduce(lambda x,y: x*y, prop), cal
  
recipe = dict()
for i in ingredients:
  recipe[i] = 5

def sz(r):
  tot = 0
  for i in r.keys():
    tot += r[i]
  return tot

def updateRecipe(recipe, amounts):
  idx = 0
  for i in ingredients:
    recipe[i] = amounts[idx]
    idx += 1


# slow recursive
def recipeGeneratorRecursion(depth, s, rec, level):
  if int(depth) == int(level):
    yield [s] + rec
  else:
    for i in range(0, s):
      for r in recipeGeneratorRecusion(depth, s - i, [i] + rec, level + 1):
        yield r

# fast hard coded
def recipeGeneratorLoops(scoops):
  for i in range(0, scoops):
    for j in range(0,scoops-i):
      for k in range(0,scoops-i-j):
        l = scoops - i - j - k
        yield [i,j,k,l]

best = False
bestR = False
#for r in recipeGeneratorRecursion(len(ingredients), scoops, [], 0):
for r in recipeGeneratorLoops(scoops):
  # Test the recipe
  updateRecipe(recipe, r)
  val = calcScore(recipe, ingredients, calAmt)
  if not best or best < val:
    bestR = dict(recipe)
    best = val

'''
s,c = calcScore(recipe, ingredients, maxCal)
print recipe, "Score:", s, "Calories:",c
'''
print "Answer: ", best, "Recipe:", bestR

# Got an answer that might be close, manually tweak the result... didn't work
"""
recipe['Frosting']      = 26
recipe['Butterscotch']  = 27
recipe['Candy']         = 23
recipe['Sugar']         = 24

s,c = calcScore(recipe, ingredients, maxCal)
print recipe, "Score:", s, "Calories:",c
"""

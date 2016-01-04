#!/usr/bin/python
import sys

start = 20151125
targetY = 2978
targetX = 3083

def calcit():
  x=1
  y=1
  maxX=1
  n = 20151125
  while True:
    n = n * 252533 % 33554393
    if x == maxX:
      maxX +=1
      x = 1
      y = maxX
    else:
      x += 1
      y -= 1
    if x == targetX and y == targetY:
      return n

print "Day 25:", calcit()

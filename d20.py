#!/usr/bin/python
import sys

target = int(sys.argv[1])
start = int(sys.argv[2])
factor = int(sys.argv[3])

def calculatePresents1(houseNum):
  num = houseNum
  total = 0
  while num > 0:
    if (houseNum % num) == 0:
      total += num * 10
    num -= 1
  return total

def calculatePresents2(houseNum):
  num = houseNum
  total = 0
  while num > 0:
    if (houseNum % num) == 0 and (houseNum / num) < 50:
      total += num * 11
    num -= 1
  return total

i = (start/factor)*factor
while True:
  val = calculatePresents1(i)
  if val > target:
    break
  #if i%(factor*50) == 0:
  #  print "i:("+str(i)+")",val
  i += factor

print "Part 1:", i

#i = (start/factor)*factor
while True:
  val = calculatePresents2(i)
  if val > target:
    break
  #if i%(factor*50) == 0:
  #  print "i:("+str(i)+")",val
  i += factor

print "Part 2:", i

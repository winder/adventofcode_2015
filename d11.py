#!/usr/bin/python
import sys

invalidCharacters = ('i', 'o', 'l')

startingPassword = open(sys.argv[1]).readline().rstrip()

def isValid(password):
  straight = False
  invalidLetters = False

  lastChar = '*'
  straightCount = 0
  pairs = list()
  for c in password:
    if c == lastChar and not c in pairs:
      pairs.append(c)
    if c in invalidCharacters:
      invalidLetters = True
    if straight or ord(c) == ord(lastChar) + 1:
      straightCount += 1
      if straightCount == 2:
        straight = True
    else:
      straightCount = 0
    lastChar = c
  return len(pairs) > 1 and straight and not invalidLetters

max = ord('z')
min = ord('a')

def incPassword(password):
  i = len(password) - 1
  carry = True
  while carry and i > 0:
    nextCh = ord(password[i]) + 1
    password[i] = chr(nextCh)
    if ord(password[i]) > max:
      password[i] = chr(min)
    else:
      carry = False
    i -= 1
  if carry:
    return password.insert(0, 'a')
  return password

def getNextPassword(password):
  while incPassword(password) and not isValid(password):
    continue
  return password

l = list(startingPassword)
print "Part 1:", "".join(getNextPassword(l))
print "Part 2:", "".join(getNextPassword(l))

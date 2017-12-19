import random as r
from math import sqrt

def distance(p1, p2):
  diff_x = p1[0] - p2[0]
  diff_y = p1[1] - p2[1]
  return sqrt(pow(diff_x, 2) + pow(diff_y, 2))

def targetplanner(envmap, robotpos, targetpos, basepos, numofmoves):
  dX = [-1, 0, 0, 1]
  dY = [0, -1, 1, 0]
  rows, cols = len(envmap), len(envmap[0])
  newtargetpos = targetpos
  for mind in xrange(numofmoves):
    maxdist = 0
    for iteration in xrange(1):
      direction = r.randint(0, 3)
      newX = targetpos[0] + dX[direction]
      newY = targetpos[1] + dY[direction]
      if (0 < newX < rows) and (0 < newY < cols):
        dist = distance([newX, newY], basepos)
        if not envmap[newX][newY] and dist > maxdist:
          newtargetpos[0] = newX
          newtargetpos[1] = newY
          maxdist = dist
          
  return newtargetpos


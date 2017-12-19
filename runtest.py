from time import sleep, time
from loader import load_map
from robotplanner import robotplanner
from targetplanner import targetplanner

def runtest(mapfile, robotstart, targetstart):
  envmap = load_map(mapfile)
  robotpos = robotstart
  targetpos = targetstart
  numofmoves = 0
  caught = False
  for i in xrange(2000):
    t0 = time()
    newrobotpos = robotplanner(envmap, robotpos, targetpos)
    t1 = time()
    diff_t = t1 - t0
    target_moves = max([1, diff_t / 0.2])
    # make the moves
    newtargetpos = targetplanner(envmap, robotpos, targetpos, targetstart, target_moves);
    robotpos = newrobotpos;
    targetpos = newtargetpos;
    numofmoves = numofmoves + 1;
    # check if target is caught
    if robotpos == targetpos:
      caught = True
      break

  print 'target caught: {} number of moves made=: {}\n'.format(caught, numofmoves)
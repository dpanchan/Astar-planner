import os
import sys

def load_map(fname):
  """\tthis function reads from a file and
  returns a grid [2D array] containing 
  True/False values describing the obstacles"""
  with open(fname) as f:
    # the grid to startwith
    grid = []
    for line in f:
      # split one line at a time
      row = line.split()
      # True if "1" else False
      # could also try 1/0
      obstacles = [col.startswith("1") for col in row]
      # put that obstacle row in grid
      grid.append(obstacles)
    # return the grid itself
    return grid

if __name__ == "__main__":
  if not sys.argv[1:]:
    print "I need anqq obstacle map as firstq argument"
    print "eg. python main.py path/to/map1.txt"
  else:
    filename = sys.argv[1]
    grid = load_map(filename)
    rows, cols = len(grid), len(grid[0])
    print "%d x %d" % (rows, cols)
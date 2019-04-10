import sys
import math

"""
Deploy the gopher to given (x, y) coordinate, and get back the actual prepared cell.

:param x: x-coordinate to deploy gopher to. 2 <= x <= 999.
:param y: y-coordinate to deploy gopher to. 2 <= y <= 999.
:return: tuple of (x, y) coordinates of cell that the gopher actually prepared.
         Returned coordinates are in range 1 to 1000 inclusive (delta of 1 from deployed coordinates).
         If we passed, then this will return (0, 0).
"""
def deploy_gopher(x, y):
  print("{:d} {:d}".format(x, y))
  sys.stdout.flush()
  actual_cell_prepared = input().split()
  return (int(actual_cell_prepared[0]), int(actual_cell_prepared[1]))

def go_gopher(min_area):
  # Note we have max. of 1000 deployments.
  # STRATEGY: Consider worst case of min_area = 200 for Test Case 2.
  # Assume we will deploy in the center of 3x3 grid sections, until the entire 3x3 grid is filled.
  # So to meet min_area = 200, we will need 23 3x3 grids next to each other (making a 3x69 rectangle
  # of area 207).
  # If we divide the 1000 deployments among the 23 3x3 grids, then we have 1000/23 = 43 deployments/grid.
  # P(grid not filled after 43 deployments) = (8/9)^43 ~= 0.0063 (negligible).
  # TODO: check the math checks out.
  deploy_x = list(range(2, math.ceil(min_area/9)*3, 3))
  for x in deploy_x:
    # Keep deploying at the centre until the entire 3x3 grid is filled.
    filled_coords = []
    while len(filled_coords) < 9:
      prepared_coord = deploy_gopher(x, 2)
      if prepared_coord == (0, 0):
        # We're finished!
        return
      if prepared_coord not in filled_coords:
        filled_coords.append(prepared_coord)

def main():
  num_cases = int(input())
  for i in range(num_cases):
    min_area = int(input())
    go_gopher(min_area)

if __name__ == "__main__":
  main()

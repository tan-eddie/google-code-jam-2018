def is_even_split_possible(rows, columns, h_cuts, v_cuts, grid):
  # To determine whether even split is possible, we need to be able to evenly divide
  # the sum of each column by v_cuts, and the sum of each row by h_cuts.
  # So let's check that.
  row_sum = []
  column_sum = [0] * columns
  grand_total = 0
  for row in grid:
    r_sum = 0
    for i in range(len(row)):
      r_sum += row[i]
      column_sum[i] += row[i]
      grand_total += row[i]
    row_sum.append(r_sum)

  # grand_total needs to be divisble by (h_cuts+1) and (v_cuts+1) (i.e. total chips in a row/column).
  if grand_total % (h_cuts + 1) != 0:
    return False
  if grand_total % (v_cuts + 1) != 0:
    return False

  row_split = grand_total / (h_cuts + 1)
  column_split = grand_total / (v_cuts + 1)
  section_split = grand_total / ((h_cuts + 1) * (v_cuts + 1))

  # We need to be able to divide on boundaries of row_split and column_split.
  cum_r_sum = 0
  h_cut_positions = []
  for i in range(len(row_sum)):
    cum_r_sum += row_sum[i]
    if cum_r_sum == row_split:
      h_cut_positions.append(i)
      cum_r_sum = 0
    elif cum_r_sum > row_split:
      return False

  cum_c_sum = 0
  v_cut_positions = []
  for i in range(len(column_sum)):
    cum_c_sum += column_sum[i]
    if cum_c_sum == column_split:
      v_cut_positions.append(i)
      cum_c_sum = 0
    elif cum_c_sum > column_split:
      return False

  # Finally, verify that the cuts produce equal chip amounts for each section.
  h_cut_positions.insert(0, -1)
  v_cut_positions.insert(0, -1)
  for h in range(len(h_cut_positions)-1):
    for v in range(len(v_cut_positions)-1):
      section_sum = 0
      for r in range(h_cut_positions[h]+1, h_cut_positions[h+1]+1):
        for c in range(v_cut_positions[v]+1, v_cut_positions[v+1]+1):
          section_sum += grid[r][c]
      if section_sum != section_split:
        return False

  # If we get here, then it's possible.
  return True

def main():
  num_cases = int(input())
  for i in range(num_cases):
    params = input().split()
    rows = int(params[0])
    columns = int(params[1])
    h_cuts = int(params[2])
    v_cuts = int(params[3])
    grid = []
    for r in range(rows):
      column = []
      row = input()
      for c in row:
        if c == "@":
          column.append(1)
        elif c == ".":
          column.append(0)
      grid.append(column)
    result = is_even_split_possible(rows, columns, h_cuts, v_cuts, grid)
    if result:
      print("Case #{:d}: POSSIBLE".format(i+1))
    else:
      print("Case #{:d}: IMPOSSIBLE".format(i+1))

if __name__ == "__main__":
  main()

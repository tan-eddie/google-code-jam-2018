# Return min number of hacks (swap of adjacent instructions)
# in p so that total damage <= d.
# If impossible, return -1
def min_hacks(d, p):

  # list containing number of shoot commands per
  # damage level. Each element is represents a
  # damage level; 1, 2, 4, 8, ... and so on.
  shots = [0]
  damage = 0
  for c in p:
    if c == "S":
      shots[-1] += 1
      # we can also calculate damage here.
      damage += 2 ** (len(shots) - 1)
    else:
      shots.append(0)

  # each hack represents moving 1 shot down 1 element
  # in the shots list. So keep doing this until
  # damage is <= d.
  hacks = 0
  while damage > d:
    # move 1 shot from highest element possible down 1 element.
    hacked = False
    for i in range(len(shots)-1, 0, -1):
      if shots[i] > 0:
        shots[i] -= 1
        shots[i-1] += 1
        damage -= 2 ** (i - 1) # damage = damage - 2**i + 2**(i-1)
        hacks += 1
        hacked = True
        break

    if not hacked:
      # impossible to get damage <= d!
      return -1

  return hacks

num_cases = int(input())
for i in range(1, num_cases+1):
  current_case = input().split()
  d = int(current_case[0])
  p = current_case[1]
  solution = min_hacks(d, p)
  if solution < 0:
    solution_string = "IMPOSSIBLE"
  else:
    solution_string = str(solution)
  print("Case #{:d}: {:s}".format(i, solution_string))
  

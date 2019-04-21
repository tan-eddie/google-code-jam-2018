import math

class Cashier:
  def __init__(self, M, S, P):
    self.M = M # Maximum bits this cashier can handle.
    self.S = S # Seconds to scan each item.
    self.P = P # Seconds to handle/package (constant for all bit numbers).

def optimal_time(R, B, cashiers, max_S, max_P):
  # Distribute B bits among R robots, where each robot is assigned a UNIQUE cashier, such
  # that time taken to process all purchases is minimal.
  # Note that robots with zero bits do not need to go through a cashier.

  # Solution strategy based on official analysis.
  # We will do a binary search on the function can_finish(T) = whether it is possible
  # to purchase the bits in the given time T.

  # Note that the max. time <= max_S * B + max_P. So start at half of this.
  lower = 0
  upper = max_S * B + max_P
  while upper-lower != 1:
    T = (lower + upper) // 2
    can_fin = can_finish(R, B, cashiers, T)
    if can_fin:
      upper = T
    else:
      lower = T

  return upper

def can_finish(R, B, cashiers, T):
  # Calculate max. number of bits each cashier can process in time T.
  max_cashier_bits = [max(0, min(c.M, math.floor((T-c.P)/c.S))) for c in cashiers]

  # Sort max_cashier_bits in decreasing order.
  max_cashier_bits.sort(reverse=True)

  # Check if we can process B bits using at most R robots (going to the cashiers that can
  # process the most bits first).
  processed_bits = 0
  robots_used = 0
  for b in max_cashier_bits:
    processed_bits += b
    robots_used += 1
    if robots_used > R:
      # Too many robots used.
      return False
    if processed_bits >= B:
      # Reached our goal!
      return True

  # Shouldn't get here because R <= C, but return False anyways.
  return False

def main():
  num_cases = int(input())
  for i in range(num_cases):
    params = input().split()
    R = int(params[0]) # Number of robots.
    B = int(params[1]) # Number of bits.
    C = int(params[2]) # Number of cashiers, note that R <= C.
    cashiers = []
    max_S = 0
    max_P = 0
    for j in range(C):
      c_params = [int(x) for x in input().split()]
      if c_params[1] > max_S:
        max_S = c_params[1]
      if c_params[2] > max_P:
        max_P = c_params[2]
      cashiers.append(Cashier(c_params[0], c_params[1], c_params[2]))
    result = optimal_time(R, B, cashiers, max_S, max_P)
    print("Case #{:d}: {:d}".format(i+1, result))

if __name__ == "__main__":
  main()

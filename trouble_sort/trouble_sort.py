
"""
Determine result of Trouble Sort.

:param v: list of numbers to sort.
:return: index of sorting error, or -1 if list will be sorted. 
"""
def trouble_sort_predictor(v):
  # Trouble sort is essentially bubble sorts on two interleaved lists.
  # List 1 is all the even elements.
  # List 2 is all the odd elements.
  # So let's separate out the two lists, sort them independently
  # (using something efficient like Python's built in sort(), and work out
  # whether there will be an error.
  v_even = v[0::2]
  v_odd = v[1::2]
  v_even.sort()
  v_odd.sort()
  # Note that len(v_even) always >= len(v_odd)
  for i in range(len(v_even)):
    # Compare with odd behind.
    if i > 0:
      if v_odd[i-1] > v_even[i]:
        return 2 * i - 1

    # Compare with odd ahead.
    if i >= len(v_odd):
      # Reached end of list.
      break
    elif v_even[i] > v_odd[i]:
      return 2 * i

  return -1

def main():
  num_tests = int(input())
  for i in range(1, num_tests+1):
    n = input()
    v = list(map(int, input().split()))
    result = trouble_sort_predictor(v)
    result_str = str(result)
    if result == -1:
      result_str = "OK"
    print("Case #{:d}: {:s}".format(i, result_str))

if __name__ == "__main__":
    main()

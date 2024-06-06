"""
5. Write a program that finds all pairs of elements in a list whose sum is equal to a given value.
"""

def find_pairs_with_sum(nums, target):
  """
  Finds all pairs of elements in a list whose sum is equal to a given value.

  Args:
      nums: A list of integers.
      target: The target sum to search for.

  Returns:
      A list of pairs (tuples) where each pair represents two elements from the list that add up to the target.
  """
  seen = set()
  result = []
  for num in nums:
    complement = target - num
    if complement in seen:
      result.append((complement, num))
    seen.add(num)
  return result

# Example usage
nums = [1, 3, 7, 9, 2]
target = 10
pairs = find_pairs_with_sum(nums, target)
print(f"Pairs in {nums} that sum to {target}: {pairs}")

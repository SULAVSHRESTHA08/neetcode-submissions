
# APPROACH: Put all nums in a set() for O(1) lookups. For each num,
# only count a sequence if it's a STARTING number (num-1 not in set) -
# this guarantees every number is counted once, total, so it's O(n)
# instead of O(n log n) with sorting. From a start, walk forward
# (num, num+1, num+2, ...) while each value is in the set, tracking
# the max length seen.
#
# HOW TO RESTART IF STUCK:
# 1. Build set(nums) for O(1) "does this exist?" checks.
# 2. For each num, ask: is num-1 in the set? If yes, skip (not a start).
# 3. If num-1 is NOT in the set, count forward from num until the
#  streak breaks; update longest.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      num_set = set(nums) 
      longest = 0
      for num in nums:
       length = 0  
       # Checking if the num is the starting number 
       if (num - 1) not in num_set:

        while (num + length) in num_set:
          length +=1
        longest = max(length,longest)  
      return longest

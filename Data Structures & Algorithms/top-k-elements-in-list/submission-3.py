from operator import itemgetter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
     count = Counter(nums)    
     # 1. Get pairs: (number, frequency)
     # Example: [(3, 1), (0, 2), (1, 1)]
     
     # 2. Sort these pairs by the frequency (the 2nd item, index 1) in descending order
     sorted_by_freq = sorted(count.items(), key = itemgetter(1), reverse=True)
     # Now sorted_items is: [(0, 2), (3, 1), (1, 1)]
     # The number 0 is still attached to its frequency 2.

     # 3. Extract just the numbers
     top = []

     for num,freq in sorted_by_freq: # unpack the number and frequency from the tuple
      top.append(num)
      if len(top) == k:
        return top      
  
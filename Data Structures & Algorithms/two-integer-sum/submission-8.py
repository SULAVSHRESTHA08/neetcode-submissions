class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preValue = {} # holds the value and its index 
        for i, n in enumerate(nums): # i: index and n : value 
          diff = target - n 
          if diff in preValue:
            return [preValue[diff], i]
          preValue[n] = i     
        return  
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       preValue = {}
       for i, n in  enumerate(nums):
        diff = target - n
        if diff in preValue:
          return [preValue[diff],i] 
        preValue[n] = i  
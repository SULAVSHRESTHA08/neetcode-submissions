class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      appear = set()
      for i in range( len(nums)):
        if nums[i] in appear:
         return True
        appear.add(nums[i])  
      return False  
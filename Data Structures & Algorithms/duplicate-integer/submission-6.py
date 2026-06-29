class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     hash = []
     for n in range (len(nums)):
      if nums[n] in hash:
       return True
      else:   
       hash.append(nums[n])
     return False
     
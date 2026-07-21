class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       box = [1] * len(nums)
       prefix = 1 
       for i in range(len(nums)):
        box[i] = prefix 
        prefix = prefix * nums[i]
 
       postfix = 1
       for i in range(len(nums)-1,-1,-1):
        box[i] = box[i] * postfix
        postfix = postfix * nums[i]
        
       return box

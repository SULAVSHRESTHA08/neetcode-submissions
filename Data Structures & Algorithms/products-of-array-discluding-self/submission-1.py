# ALGORITHM: Prefix * Postfix (2-Pass)
# 1. PREFIX PASS (L->R): box[i] = product of all elements to the LEFT.
#    Ex: [1, 2, 3, 4] -> box becomes [1, 1, 2, 6]
# 2. POSTFIX PASS (R->L): Multiply box[i] by product of all elements to the RIGHT.
#    Ex: [1, 1, 2, 6] * [24, 12, 4, 1] -> Final: [24, 12, 8, 6]
# KEY: 'prefix' tracks left product, 'postfix' tracks right product. No division used.

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

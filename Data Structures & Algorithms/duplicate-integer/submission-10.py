class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appear = set()
        for num in nums:
            if num not in appear:
                appear.add(num)
            else:
                return True 
        return False           
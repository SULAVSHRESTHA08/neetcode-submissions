class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
     return sorted(s) == sorted(t) # sorting an element and checking its validity   
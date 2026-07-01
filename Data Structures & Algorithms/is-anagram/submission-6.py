class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t): # initial check if the the len of string is not equal then return false  
       return False
      else:
        countS , countT = {}, {}
        
        for i in range(len(s)):
          countS[s[i]] = countS.get(s[i], 0) + 1  # Counts the occurence of each element 
          countT[t[i]] = countT.get(t[i], 0) + 1
        return countS == countT # CHecks if equal  
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
          return False
        else:
          countS = {} # Creating hash table for the count of s
          countT = {} # Creating hash table for the count of table
          for i in range(len(s)):
           countS[s[i]] = countS.get(s[i],0) + 1
           countT[t[i]] = countT.get(t[i],0) + 1
          return countT == countS
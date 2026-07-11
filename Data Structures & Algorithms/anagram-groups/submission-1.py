class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      result = defaultdict(list)   # maping character count to list of Anagrams 
      for s in strs:
        count = [0] * 26 # 26 character from a to z
         
        for c in s:
          count[ord(c) - ord("a")] +=1 

        result[tuple(count)].append(s)  

      return list(result.values()) 
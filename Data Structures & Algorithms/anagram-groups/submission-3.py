class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      pairs  = {} #Mapping the charcater count to list of Anagrams 
      for s in strs :
        count = Counter(s) # Create a count of characters for the current string
        # Convert the Counter to a tuple of sorted items to make it hashable 
        key = tuple(sorted(count.items())) # signature for the anagrams 

        if key not in pairs:
          pairs[key] = []  # creates an empty list on demand for a new key.
        pairs[key].append(s)
      return list(pairs.values())        
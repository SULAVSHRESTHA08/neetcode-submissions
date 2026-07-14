class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      count = Counter(nums) # create a dictonary of values and its frequency 
      
      bucket = [[] for i in range(len(nums)+1)] # Creates an empty bucket which has length of total numbers in nums.  
  
      # update the bucket where frequency act as array index 
      # and number act as their respective elements     
      for number, frequency in count.items():
        bucket[frequency].append(number)  
      
      top_K =[]
   
      for i in range(len(bucket)-1, 0 , -1):  #Reverse the numbers for decending values
        for number in bucket[i]:  # check the values
          top_K.append(number)    # append the values in top_k list

          if  len(top_K) == k:    # Stops when the array reaches its need(k)
           return list(top_K)  

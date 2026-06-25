class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
    # Hashmap solution
    # my_map = {}
    # for i in range()    
    
    # Brute Force solution
    # Log n2
         
        for i in range(len(nums)):
            for j in range(i +1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [min(i,j), max(i,j)]
        return[0,0]

         
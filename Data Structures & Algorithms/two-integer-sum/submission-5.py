class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
    # Hashmap solution
    # You create a hashmap to store see if you have the complement to the number youre on
    # If you have that complement in your list you then pull the index of where it is stored
    # as its value
    
        my_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in my_map:
                return [my_map[complement], i]   
            my_map[num] = i
    
    # Brute Force solution
    # Log n2
        # for i in range(len(nums)):
        #     for j in range(i +1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [min(i,j), max(i,j)]
        # return[0,0]

         
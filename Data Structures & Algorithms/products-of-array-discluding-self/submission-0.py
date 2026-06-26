class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Brute Force Solution
        arr = []
        for i in range(0,len(nums)):
            product = 1
            for j in range(0,len(nums)):
                if j == i:
                    continue
                product *= nums[j]
            arr.append(product)



        return arr
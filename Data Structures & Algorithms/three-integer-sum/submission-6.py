class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        left = 1
        right = len(nums) - 1 

        triplets = []
        nums.sort()
        print(nums)
        
        for i in range(0,len(nums) -2):
            #skip duplicate i's
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1 

            while left < right:
                
                is_zero = nums[i] + nums[left] + nums[right]
                
                if is_zero == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                            left += 1
                    while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                    # left += 1
                    # right -= 1
                if is_zero < 0:
                    left += 1
                else:
                    right -= 1
                    
        return [] if not triplets else triplets
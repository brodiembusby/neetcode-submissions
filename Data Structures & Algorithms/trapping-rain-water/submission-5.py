class Solution:
    def trap(self, height: List[int]) -> int:
            
        #Brute Force Solution
        # left_max = 0
        # right_max = 0
        # water = 0
        # length = len(height)
        # for i in range(1,length):
        #         # Find tallest bar to the left
        #         # Find tallest bar to the right
        #         # Calculate water above this bar
        #         # Add it to the total
        #     left_max = 0
        #     right_max = 0

        #     for l in range(i,-1,-1):
        #         left_max = max(height[l],left_max)
        #     for r in range(i,length):
        #         right_max = max(height[r],right_max)
        #     water += min(left_max, right_max) - height[i]

        # return water 
        left = 0
        right = len(height) - 1
        
        left_max = height[left]
        right_max = height[right]
        
        water = 0
        while left < right:
            if left_max < right_max:
                left += 1
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
            else:
                right -= 1
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
        return water
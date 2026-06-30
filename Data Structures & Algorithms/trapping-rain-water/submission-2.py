class Solution:
    def trap(self, height: List[int]) -> int:
        
        # #if right taller than left move right
        # # if left taller than right move right
        # left = 0
        # # Can't have water if left + 1
        # right = left + 2
        
        # area_water = 0
        # water_height = 0
       
       
        left_max = 0
        right_max = 0
        water = 0
        total = 0
        length = len(height)
        for i in range(1,length):
                # Find tallest bar to the left
                # Find tallest bar to the right
                # Calculate water above this bar
                # Add it to the total
            left_max = 0
            right_max = 0

            for l in range(i,-1,-1):
                left_max = max(height[l],left_max)
            for r in range(i,length):
                right_max = max(height[r],right_max)
            water += min(left_max, right_max) - height[i]
            # total += max(0,water)   

        return water 
   
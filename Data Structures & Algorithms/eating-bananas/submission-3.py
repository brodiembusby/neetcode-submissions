class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Brute Force 
        # Chatgpt explained as koko can only east from one pile at a time
        # at a defined speed. So we go from 1 banana all the way to the biggest
        # pile if hours is <= h then we found our minimum speed to eat it
        # all.
            
        
        # for speed in range(1,max(piles) + 1):
        #     hours = 0

        #     for pile in piles:
                
        #         hours += math.ceil(pile / speed)
            
        #     if hours <= h:
        #         return speed
        # return max(piles)

        # Slowest eating speed
        left = 1
        # fastest eating speed
        right = max(piles) + 1

        while left < right:

            mid = (left + right) // 2
            
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours > h:
                left = mid + 1
            else:
                right = mid
        return left






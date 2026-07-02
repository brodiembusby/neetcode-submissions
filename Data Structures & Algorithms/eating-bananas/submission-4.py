class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
   
    # Coming back to see if I understood solution

        right = max(piles) + 1
        left = 1

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
            

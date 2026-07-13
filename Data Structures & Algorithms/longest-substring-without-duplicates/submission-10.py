class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
                
        if len(s) < 1:
            return 0
        left = 0
        right = 1
        
        total = 1
        my_set = set(s[0])

        
        while right < len(s):

            if s[right] not in my_set:
                my_set.add(s[right])
                total = max(len(my_set),total)
                right += 1
            else:
                my_set.remove(s[left])
                left += 1
                
            
        return total
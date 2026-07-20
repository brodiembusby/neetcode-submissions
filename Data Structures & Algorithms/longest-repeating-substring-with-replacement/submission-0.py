class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        left = 0
        right = 1
        total = 1
        my_map = {s[left] : 1}

        while right < len(s):
            
            if s[right] in my_map:
                my_map[s[right]] += 1
            else:
                my_map[s[right]] = 1

            if (right - left + 1) - max(my_map.values()) > k:
                my_map[s[left]] -= 1
                left += 1
            total = max(total,sum(my_map.values()))
            right += 1
        return total
                     
                    
        
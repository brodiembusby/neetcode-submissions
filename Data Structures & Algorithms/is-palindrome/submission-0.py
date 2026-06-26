import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_up = "".join(s.split())
        clean_up = re.sub(r'[^a-zA-Z0-9]','',clean_up)
        clean_up= clean_up.lower()
        p1 = 0
        p2 = len(clean_up) - 1
        while(p1 < p2):  
            if clean_up[p1] != clean_up[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True
        
        
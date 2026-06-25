class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {}
        hashmap_t = {}
        for key in s:
            hashmap_s[key] = hashmap_s.get(key, 0) + 1
        for key in t:
            hashmap_t[key] = hashmap_t.get(key, 0) + 1
        if hashmap_s == hashmap_t:
            return True
        else:
            return False
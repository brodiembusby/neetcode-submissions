class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = {}
        
        for string in strs:
            sorted_text = "".join(sorted(string))
            if sorted_text in my_map:
                my_map[sorted_text].append(string) 
            else:
                my_map[sorted_text] = [string]
        return list(my_map.values())
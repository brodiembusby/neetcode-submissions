class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # A map to hold amount of times item appeared
        my_map = {}
        total = []
        for i in nums:
            if i in my_map:
                my_map[i] += 1
            else:
                my_map[i] = 1
        # Sort the list so most frequent items how up at the beginning
        sorted_list = list(sorted(my_map.items(), key=lambda item: item[1], reverse=True))
        # Add Most frequent items to total
        for key in range(0,k):
            total.append(sorted_list[key][0])
        return total
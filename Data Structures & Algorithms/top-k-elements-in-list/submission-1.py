class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        my_map = {}
        for i in nums:
            if i in my_map:
                my_map[i] += 1
            else:
                my_map[i] = 1
        # sort if needed
        sorted_list = list(sorted(my_map.items(), key=lambda item: item[1]))
        total = []
        # print(sorted_list)
        sorted_list = sorted_list[::-1]
        for key in range(0,k):
            total.append(sorted_list[key][0])
        return total
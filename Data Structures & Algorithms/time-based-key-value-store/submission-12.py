class TimeMap:


    def __init__(self):
        
        self.my_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        

        if key in self.my_map:
            self.my_map[key].append([timestamp,value])
            # print(self.my_map)
        else:
            self.my_map[key] = [[timestamp,value]]
        # print(self.my_map)

    def get(self, key: str, timestamp: int) -> str:
       
        if key not in self.my_map:
            return ""

        # how do i retrieve the first element in the list
        left = 0
        # how do i retrieve the last elements first index
        right = len(self.my_map[key]) - 1
        print(right)

        while left <= right:

            mid = (left + right) // 2

            # if mid == timestamp and in my_map then return
            # value at that location
            if self.my_map[key][mid][0] == timestamp:
                return self.my_map[key][mid][1]
            elif self.my_map[key][mid][0] < timestamp:
                left = mid + 1

            else:
                right = mid - 1
        print(self.my_map)
        print(right)
        print(left)
        if right == -1:
            return ""

        return self.my_map[key][right][1]

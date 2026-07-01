class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        l1 = 0
        r1 = len(matrix) - 1
        print(matrix[0][0])

        while l1 <= r1:
            
            row_mid = (l1 + r1) // 2
           
            if matrix[row_mid][0] <= target <= matrix[row_mid][-1]:
                l2 = 0
                r2 = len(matrix[row_mid]) - 1
                while l2 <= r2:
                    col_mid = (l2 + r2) // 2
                    if matrix[row_mid][col_mid] < target:
                        l2 = col_mid + 1
                    elif matrix[row_mid][col_mid] > target:
                        r2 = col_mid - 1
                    elif matrix[row_mid][col_mid] == target:
                        return True
                return False
            elif target > matrix[row_mid][0]:
                    l1 = row_mid + 1
            else:
                r1 = row_mid - 1


        return False
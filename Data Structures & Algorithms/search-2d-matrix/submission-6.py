class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l1 = 0
        r1 = len(matrix) - 1
        print(matrix[0][0])

        # Binary Search the first element in the rows
        while l1 <= r1:
            
            row_mid = (l1 + r1) // 2
           
            # If the target is between the first and the last amount
            # in this row binary search that row
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
                # If it is not in this row then it won't be anywhere else
                # because of the constraints so we return False
                return False
            elif target > matrix[row_mid][0]:
                    l1 = row_mid + 1
            else:
                r1 = row_mid - 1
        
        return False
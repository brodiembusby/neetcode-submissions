class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(0,9,3):
            for col in range(0,9,3):
                
                square = [r[col:col+3] for r in board [row:row+3]]
                if not self.isValidSquare(square):
                    return False
        
        # Check Rows
        for row in range(0,9):
            my_set = set()
            arr = []
            for col in range(0,9):
                tile = board[row][col]
                if tile.isalnum():
                    my_set.add(tile)
                    arr.append(tile)
            if len(my_set) != len(arr):
                return False
        # Check Columns
        for col in range(0, 9):
            my_set = set()
            arr = []
            for row in range(0, 9):
                tile = board[row][col]
                if tile.isalnum():
                    my_set.add(tile)
                    arr.append(tile)
            if len(my_set) != len(arr):
                return False

        return True
            
    
    
    
    def isValidSquare(self, square):
        my_set = set()
        arr = []
        for i in range(0,3):
            for j in range(0,3):
                tile = square[i][j]

                if tile.isalnum():
                    my_set.add(tile)
                    arr.append(tile)

        return True if len(my_set) == len(arr) else False
            
            
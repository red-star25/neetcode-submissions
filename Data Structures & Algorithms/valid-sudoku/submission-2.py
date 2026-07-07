class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        for row in range(ROWS):
            hmRow = {}
            for col in range(COLS):
                if board[row][col] != ".":
                    if board[row][col] in hmRow:
                        return False
                    hmRow[board[row][col]] = True
                
        for col in range(COLS):
            hmCol = {}
            for row in range(ROWS):
                if board[row][col] != ".":
                    if board[row][col] in hmCol:
                        return False
                    hmCol[board[row][col]] = True
        
        for i in range(3):
            for j in range(3):
                hmBox = {}  
                for l in range(3):
                    for m in range(3):
                        row = i * 3 + l
                        col = j * 3 + m
                        val = board[row][col]
                        
                        if val != ".":
                            if val in hmBox:
                                return False
                            hmBox[val] = True

            
        return True
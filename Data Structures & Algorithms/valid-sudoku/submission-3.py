class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        for row in range(ROWS):
            hmR = {}
            for col in range(COLS):
                if board[row][col] in hmR and board[row][col] != ".":
                    return False
                hmR[board[row][col]] = True
        
        for row in range(ROWS):
            hmC = {}
            for col in range(COLS):
                if board[col][row] in hmC and board[col][row] != ".":
                    return False
                hmC[board[col][row]] = True
        

        for i in range(ROWS // 3):
            for j in range(COLS // 3):
                hmS = {}
                for k in range(3):
                    for l in range(3):
                        row = i * 3 + k
                        col = j * 3 + l
                        val = board[row][col]

                        if val != ".":
                            if val in hmS:
                                return False
                            hmS[val] = True

        return True
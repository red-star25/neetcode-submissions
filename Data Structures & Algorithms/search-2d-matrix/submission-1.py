class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        for row in range(ROWS):
            if matrix[row][-1] < target:
                continue
            else:
                for col in range(COLS):
                    left, right = 0, len(matrix[row]) - 1
                    
                    while left <= right:
                        mid = left + ((right - left) // 2)
                        
                        if matrix[row][mid] > target:
                            right = mid - 1
                        elif matrix[row][mid] < target:
                            left = mid + 1
                        else:
                            return True
        
        return False
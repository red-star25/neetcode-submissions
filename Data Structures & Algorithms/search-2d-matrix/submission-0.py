class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            print(m)
            l = 0
            r = len(m) - 1

            while l <= r:
                mid = l + (r-l) // 2

                if m[mid] < target:
                    l = mid + 1
                elif m[mid] > target:
                    r = mid - 1
                else:
                    return True
        return False
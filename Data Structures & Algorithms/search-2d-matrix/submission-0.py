class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen = len(matrix)
        colLen = len(matrix[0])
        low = 0
        high = rowLen * colLen - 1
        while low <= high:
            mid = int((low +high) / 2)
            row = int(mid/colLen)
            col = mid%colLen
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False

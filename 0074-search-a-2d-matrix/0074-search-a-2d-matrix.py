class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while r >= l:
            mid = int((r + l) / 2)
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1
        if not (matrix[mid][0] <= target <= matrix[mid][-1]):
            return False
        
        l = 0
        r = len(matrix[0]) - 1
        while r >= l:
            mid2 = int((r + l) / 2)
            if matrix[mid][mid2] == target:
                return True
            elif matrix[mid][mid2] > target:
                r = mid2 - 1
            else:
                l = mid2 + 1
        return False
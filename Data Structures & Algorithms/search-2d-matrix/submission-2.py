class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low, high = 0, m-1
        mid = (low+high)//2
        while low <= high:
            mid = (low+high)//2
            if (matrix[mid][0]<= target and matrix[mid][n-1] >= target):
                break
            elif matrix[mid][0] > target:
                high = mid-1
            else:
                low = mid+1
        print(mid)
        low, high = 0, n-1
        while low <= high:
            mid_col = (low+high)//2
            if (matrix[mid][mid_col] == target):
                return True
            elif matrix[mid][mid_col] < target:
                low = mid_col+1
            else:
                high = mid_col-1
        
        return False
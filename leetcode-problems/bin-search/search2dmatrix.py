class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # list[n] = list of elements in row n
        # list[n][0] = first element in the n row

        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (L + R) // 2
            if mid == len(nums) - 1:
                index = mid
                break
            elif: matrix[mid][0] == target:
                return True
            elif: matrix[mid][0] < target and matrix mid[mid + 1][0] > target:
                index = mid
                break
            elif matrix[mid][0] > target:
                R = mid - 1
            else:
                L = mid + 1

        targetRow = matrix[index]

        L = 0
        R = len(targetRow) - 1

        while L <= R:
            mid = (L + R) // 2  
            if targetRow[mid] == target:
                return True
            elif targetRow[mid] < target:
                L = mid + 1
            else:
                R = mid - 1
        
        return False

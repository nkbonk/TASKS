'''
https://leetcode.com/problems/search-a-2d-matrix/

Time: O(log(m * n)). Условие задачи сделать такое время. Долго думал над этим.
Space: O(1)
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            row, col = mid // n, mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

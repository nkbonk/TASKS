'''
https://leetcode.com/problems/koko-eating-bananas/description/

Time: O(n)
Space: O(1)
'''


class Solution(object):
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            if sum((p + mid - 1) // mid for p in piles) <= h:
                right = mid
            else:
                left = mid + 1
        return left

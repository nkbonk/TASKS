'''
https://leetcode.com/problems/time-based-key-value-store/description/

Time: (смотри в файле)
Space: O(n)
'''


class TimeMap:
    def __init__(self):
        self.store = {}

    # Time: O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    # Time: O(log n)
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        arr = self.store[key]
        left, right = 0, len(arr) - 1
        res = ""
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return res

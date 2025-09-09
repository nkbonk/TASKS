'''
https://leetcode.com/problems/longest-repeating-character-replacement/

Time: O(n), там в люьом случае один проход
Space: O(1)
'''


class Solution:
    def characterReplacement(self, s, k):
        count = {}
        max_freq = 0
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
            
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = {}
        left = 0
        maxCount = 0
        for right, n in enumerate(s):
            if n in hashSet and hashSet[n] >= left:
                left = hashSet[n] + 1
            hashSet[n] = right
            maxCount = max(maxCount, right-left+1)
        return maxCount
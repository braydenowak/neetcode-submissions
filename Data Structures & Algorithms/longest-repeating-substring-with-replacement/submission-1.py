class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxCount = left = maxF = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxF = max(maxF, count[s[right]])

            while (right - left + 1) - maxF > k:
                count[s[left]] -= 1
                left += 1
            maxCount = max(maxCount, right - left + 1)

        return maxCount
            

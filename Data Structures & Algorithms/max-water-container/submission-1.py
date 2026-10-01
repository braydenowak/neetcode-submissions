class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right, maxA = 0, len(heights)-1, 0
        while left < right:
            if min(heights[left],heights[right])*(right-left) > maxA:
                maxA = min(heights[left],heights[right])*(right-left)
                continue
            if heights[left]< heights[right]:
                left += 1
            else:
                right -= 1

        return maxA
            
                
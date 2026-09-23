class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)
        prefix[0] = nums[0]
        suffix[len(nums)-1] = nums[len(nums)-1]
        result = [0]*len(nums)
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
            suffix[len(nums)-1-i] =  suffix[len(nums)-i] * nums[len(nums)-1-i]


        for i in range(0,len(nums)):
            left = prefix[i-1] if i > 0 else 1
            right = suffix[i+1] if i < len(nums)-1 else 1
            result[i] = left * right

        return result